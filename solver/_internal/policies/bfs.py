from ..explorer.explorer import Explorer
from ..log import log
from ..explorer.move import Move

logger = log.logger()

def bfs(initial_state, goal_state):
    logger.info("Starting BFS run.")

    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    frontier = [(initial_state, Move.moves_from(initial_state))]
    explorer = Explorer(initial_state)
    while len(frontier) > 0 and not found_goal:
        state, moves = frontier.pop(0)

        for move in moves:
            next_state = move.mutate(state)
            if not explorer.is_state_new(next_state):
                continue
            explorer.update_head(state, next_state, move)
            if next_state == goal_state:
                found_goal = True
                break
            next_moves = explorer.branch()
            frontier.append((next_state, next_moves))


    if found_goal:
        logger.info("Finished BFS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished BFS run. Did not find goal.")
        return None
