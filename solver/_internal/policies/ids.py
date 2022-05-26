from _internal.explorer.explorer import Explorer
from _internal.log import log
from _internal.explorer.move import Move

logger = log.logger()


def ids(initial_state, goal_state):
    logger.info("Starting BFS run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    def should_reset(depth_iteration, cur_level):
        return (cur_level+1) % depth_iteration == 0

    frontier = [(initial_state, Move.moves_from(initial_state))]
    next_frontier = []
    explorer = Explorer(initial_state)
    depth_iteration = 2
    levels 
    cur_level = 0
    while not found_goal and (len(frontier) > 0 or len(next_frontier) > 0):

        state, moves = frontier.pop()

        for move in moves:
            next_state = move.mutate(state)
            if not explorer.is_state_new(next_state):
                continue
            explorer.update_head(state, next_state, move)
            if next_state == goal_state:
                found_goal = True
                break
            next_moves = explorer.branch()

            if should_reset(depth_iteration, cur_level):
                next_frontier.append((next_state, next_moves))
            else:
                frontier.append((next_state, next_moves))

        if len(frontier) <= 0:
            frontier = next_frontier
            next_frontier = []

    if found_goal:
        logger.info("Finished IDS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished IDS run. Did not find goal.")
        return None
