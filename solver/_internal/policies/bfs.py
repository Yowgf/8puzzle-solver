from ..explorer.explorer import Explorer
from ..log import log
from ..explorer.move import Move
from ..datastruct.queue import Queue

logger = log.logger()

def bfs(initial_state, goal_state):
    logger.info("Starting BFS run.")

    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    frontier = Queue()
    frontier.push((initial_state, Move.moves_from(initial_state)))
    explorer = Explorer(initial_state)
    while len(frontier) > 0 and not found_goal:
        state, moves = frontier.pop()

        for move in moves:
            next_state, next_moves, state_new = (
                explorer.update_head_and_branch(state, move))
            if not state_new:
                continue
            if next_state == goal_state:
                found_goal = True
                break
            frontier.push((next_state, next_moves))

    if found_goal:
        logger.info("Finished BFS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished BFS run. Did not find goal.")
        return None
