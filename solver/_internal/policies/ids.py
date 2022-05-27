from _internal.datastruct.stack import Stack
from _internal.explorer.explorer import Explorer
from _internal.explorer.move import Move
from _internal.explorer.expansion import Expansion
from _internal.log import log

logger = log.logger()

def ids(initial_state, goal_state):
    logger.info("Starting BFS run")
    
    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    def should_reset(depth_iteration, cur_level):
        return (cur_level+1) % depth_iteration == 0

    frontier = Stack()
    frontier.push(Expansion(initial_state, Move.moves_from(initial_state)))
    next_frontier = Stack()
    explorer = Explorer(initial_state)
    depth_iteration = 2
    levels = "TODO"
    cur_level = 0
    while not found_goal and (len(frontier) > 0 or len(next_frontier) > 0):

        expansion = frontier.pop()

        for move in expansion.moves:
            expanded, state_new = explorer.update_head_and_branch(
                expansion.parent_state, move)
            if not state_new:
                continue
            if expanded.parent_state == goal_state:
                found_goal = True
                break

            if should_reset(depth_iteration, cur_level):
                next_frontier.push(expanded)
            else:
                frontier.push(expanded)

        if len(frontier) <= 0:
            frontier = next_frontier
            next_frontier = Stack()

    if found_goal:
        logger.info("Finished IDS run. Found goal.")
        return explorer.steps_to_cur_state()
    else:
        logger.info("Finished IDS run. Did not find goal.")
        return None
