from ..datastruct.queue import Queue
from ..explorer.expansion import Expansion
from ..explorer.explorer import Explorer
from ..explorer.move import Move
from .heuristics import manhattan_distance
from ..log import log

logger = log.logger()

def hclimb(initial_state, goal_state, heuristic=manhattan_distance):
    logger.info("Starting Hill Climbling run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    explorer = Explorer(initial_state)

    # In the case of Hill Climbing, the frontier always just has one Expansion.
    frontier = Queue()
    frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))

    while not found_goal and len(frontier) > 0:
        expansion = frontier.pop()

        new_expansions = []
        for move in expansion.moves:
            expanded, state_new = explorer.expand(expansion.parent_state, move)
            if not state_new:
                continue
            if expanded.parent_state == goal_state:
                found_goal = True
                break
            new_expansions.append(expanded)

        if len(new_expansions) <= 0:
            break

        heuristics = [heuristic(expansion.parent_state)
                      for expansion in new_expansions]

        expansion_with_best_heuristic = new_expansions[
            heuristics.index(min(heuristics))]

        frontier.push(expansion_with_best_heuristic)

    if found_goal:
        logger.info("Finished Hill Climbling run. Found goal.")
        return explorer.steps_to_state(goal_state)
    else:
        logger.info("Finished Hill Climbling run. Did not find goal.")
        return None
