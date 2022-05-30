from ..explorer.explorer import Explorer
from ..log import log
from ..explorer.expansion import Expansion
from ..explorer.move import Move
from ..datastruct.queue import Queue
from .utils import algorithm_results

logger = log.logger()

def bfs(initial_state, goal_state, test_explorer=None):
    logger.info("Starting BFS run.")

    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    frontier = Queue()
    frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))

    if test_explorer == None:
        explorer = Explorer(initial_state)
    else:
        # test_explorer is used only for testing purposes
        explorer = test_explorer

    while len(frontier) > 0 and not found_goal:
        expansion = frontier.pop()

        for move in expansion.moves:
            expanded, state_new = explorer.expand(expansion.parent_state, move)
            if not state_new:
                continue
            if expanded.parent_state == goal_state:
                found_goal = True
                break
            frontier.push(expanded)

    return algorithm_results(logger, 'BFS', explorer, found_goal, goal_state)
