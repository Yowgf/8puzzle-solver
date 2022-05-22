from _internal.explorer.explorer import Explorer
from _internal.log import log

logger = log.logger()

# BFS
#
# TODO: how to keep track of the steps we are taking?
def bfs(initial_state, goal_state):
    frontier = [initial_state]
    explored = []
    found_goal = False
    explorer = Explorer()
    while len(frontier) > 0 and not found_goal:
        state = frontier.pop()
        logger.debug(f"Exploring state {state}")
        if state in explored:
            continue
        else:
            explored.append(state)
            if state == goal_state:
                found_goal = True
        explorer.update_head(state)
        next_states = explorer.branch()
        frontier.extend(next_states)

    if found_goal:
        return explorer.steps_to_cur_state()
    else:
        # Indicate failure by returning None
        return None
