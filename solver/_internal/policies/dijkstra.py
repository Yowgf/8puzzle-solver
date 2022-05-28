from ..datastruct.heap import Heap
from ..explorer.expansion import Expansion
from ..explorer.explorer import Explorer
from ..explorer.move import Move
from ..log import log

logger = log.logger()


def dijkstra(initial_state, goal_state):
    logger.info("Starting Dijkstra run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    explorer = Explorer(initial_state)

    frontier = Heap()
    frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))

    while not found_goal and len(frontier) > 0:
        expansion = frontier.pop()

        

    if found_goal:
        logger.info("Finished Dijkstra run. Found goal.")
        return explorer.steps_to_state(goal_state)
    else:
        logger.info("Finished Dijkstra run. Did not find goal.")
        return None
