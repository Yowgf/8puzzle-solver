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

    frontier = Stack()
    frontier.push((initial_state, Move.moves_from(initial_state)))
    next_frontier = Stack()
    explorer = Explorer(initial_state)
    depth_iteration = 2
    levels = "TODO"
    cur_level = 0
    while not found_goal and (len(frontier) > 0 or len(next_frontier) > 0):

        state, moves = frontier.pop()

        for move in moves:
            next_state, next_moves, state_new = (
                explorer.update_head_and_branch(state, move))
            if not state_new:
                continue
            if next_state == goal_state:
                found_goal = True
                break

            if should_reset(depth_iteration, cur_level):
                next_frontier.push((next_state, next_moves))
            else:
                frontier.push((next_state, next_moves))

        if len(frontier) <= 0:
            frontier = next_frontier
            next_frontier = Stack()

    if found_goal:
        logger.info("Finished IDS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished IDS run. Did not find goal.")
        return None
