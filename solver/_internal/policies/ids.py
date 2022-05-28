from ..datastruct.stack import Stack
from ..explorer.explorer import Explorer
from ..explorer.move import Move
from ..explorer.expansion import Expansion
from ..log import log

logger = log.logger()

def _frontiers_empty(frontiers):
    for frontier in frontiers:
        if len(frontier) > 0:
            return False
    return True

def ids(initial_state, goal_state):
    logger.info("Starting BFS run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    start_frontier = Stack()
    start_frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))
    explorer = Explorer(initial_state)

    # Initializer frontiers
    deepening_rate = 3
    assert deepening_rate > 0
    # One for each level we can look further into
    frontiers = [start_frontier]
    for _ in range(deepening_rate-1):
        frontiers.append(Stack())

    # while not found_goal and not _frontiers_empty(frontiers):
    #     # Loops through different levels in a circular fashion
    #     for level in range(deepening_rate):
    #         frontier = frontiers[level]

    #         expansion = frontier.pop()
    #         def dfs(expansion):
    #             expanded, state_new = explorer.update_head_and_branch(
    #                 expansion.parent_state, move)
    #             if not state_new:
    #                 continue
    #             if expanded.parent_state == goal_state:
    #                 found_goal = True
    #                 break
                
    #             frontiers[(level+1)%deepening_rate].push(expanded)


    if found_goal:
        logger.info("Finished IDS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished IDS run. Did not find goal.")
        return None
