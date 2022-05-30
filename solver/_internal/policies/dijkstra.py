from ..explorer.expansion import Expansion
from ..explorer.explorer import Explorer
from ..datastruct.expansion_heap import ExpansionHeap
from ..explorer.move import Move
from ..log import log
from .utils import algorithm_results

logger = log.logger()


def dijkstra(initial_state, goal_state):
    logger.info("Starting Dijkstra run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    explorer = Explorer(initial_state)

    frontier = ExpansionHeap()
    frontier.push(0, Expansion(initial_state, Move.moves_from(initial_state)))

    while not found_goal and len(frontier) > 0:
        _, expansion = frontier.pop()
        
        for move in expansion.moves:
            expanded, state_new = explorer.expand(expansion.parent_state, move)
            if not state_new:
                continue
            if expanded.parent_state == goal_state:
                found_goal = True
                break

            depth = explorer.state_depth(expanded.parent_state)
            frontier.push(depth, expanded)

    return algorithm_results(logger, 'Dijkstra', explorer, found_goal, goal_state)
