from ..explorer.explorer import Explorer
from ..log import log
from ..explorer.expansion import Expansion
from ..explorer.move import Move
from ..datastruct.queue import Queue

logger = log.logger()

def bfs(initial_state, goal_state):
    logger.info("Starting BFS run.")

    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    frontier = Queue()
    frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))
    explorer = Explorer(initial_state)
    while len(frontier) > 0 and not found_goal:
        expansion = frontier.pop()

        for move in expansion.moves:
            expanded, state_new = explorer.update_head_and_branch(
                expansion.parent_state, move)
            if not state_new:
                continue
            if expanded.parent_state == goal_state:
                found_goal = True
                break
            frontier.push(expanded)

    if found_goal:
        logger.info("Finished BFS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished BFS run. Did not find goal.")
        return None
