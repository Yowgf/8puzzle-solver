from ..datastruct.stack import Stack
from ..explorer.expansion import Expansion
from ..explorer.explorer import Explorer
from ..explorer.move import Move
from ..log import log
from .utils import algorithm_results

logger = log.logger()

def ids(initial_state, goal_state):
    logger.info("Starting IDS run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    explorer = Explorer(initial_state)

    deepening_rate = 3
    cur_level = 0
    assert deepening_rate > 0
    frontier = Stack()
    frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))
    next_frontier = Stack()

    while not found_goal and (len(frontier) > 0 or len(next_frontier) > 0):
        while len(frontier) > 0:
            expansion = frontier.pop()
            parent_state = expansion.parent_state
            state_depth = explorer.state_depth(parent_state)
            for move in expansion.moves:
                expanded, state_new = explorer.expand(parent_state, move)
                if not state_new:
                    continue
                if expanded.parent_state == goal_state:
                    found_goal = True
                    break
                
                if state_depth + 1 < cur_level + deepening_rate:
                    frontier.push(expanded)
                else:
                    next_frontier.push(expanded)

        frontier = next_frontier
        next_frontier = Stack()
        cur_level += deepening_rate

    return algorithm_results(logger, 'IDS', explorer, found_goal, goal_state)
