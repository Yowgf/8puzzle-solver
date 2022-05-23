from _internal.explorer.explorer import Explorer
from _internal.log import log
from _internal.explorer.move import Move

logger = log.logger()

def state_hash(state):
        m = max(state) + 2
        sticked = 0
        for i in range(len(state)):
            sticked += (10 ** i) * state[i]
        return sticked
# BFS
#
# TODO: how to keep track of the steps we are taking?
def bfs(initial_state, goal_state):
    logger.info("Starting BFS run")

    frontier = [(initial_state, Move.moves_from(initial_state))]
    explored = []
    found_goal = False
    explorer = Explorer(initial_state)
    while len(frontier) > 0 and not found_goal:
        logger.debug(f"(BFS) New iteration. Size of frontier: {len(frontier)}")

        state, moves = frontier.pop()
        logger.debug(f"(BFS) Expanding state {state}. Hash={state_hash(state)}")

        if state not in explored:
            explored.append(state)

        for move in moves:
            next_state = move.mutate(state)
            if not explorer.is_state_new(next_state):
                logger.debug(f"State {next_state} is not new. Hash={state_hash(next_state)}")
                if next_state not in explored:
                    logger.debug("State is actually new!@#!@#")
                continue
            if next_state not in explored:
                explored.append(next_state)
            logger.debug(f"(BFS) Found new state {next_state}.")
            explorer.update_head(state, next_state, move)
            if next_state == goal_state:
                logger.debug(f"Found solution: {next_state}. Finishing search")
                found_goal = True
                break
            next_moves = explorer.branch()
            frontier.append((next_state, next_moves))

    logger.info("Finished BFS run")

    if found_goal:
        return explorer.steps_to_cur_state()
    else:
        # Indicate failure by returning None
        return None
