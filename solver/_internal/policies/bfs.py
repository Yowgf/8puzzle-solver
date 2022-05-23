from _internal.explorer.explorer import Explorer
from _internal.log import log
from _internal.explorer.move import Move

logger = log.logger()

def bfs(initial_state, goal_state):
    logger.info("Starting BFS run")

    found_goal = False
    if initial_state == goal_state:
        found_goal = True

    frontier = [(initial_state, Move.moves_from(initial_state))]
    explorer = Explorer(initial_state)
    while len(frontier) > 0 and not found_goal:
        state, moves = frontier.pop()

        for move in moves:
            next_state = move.mutate(state)
            if not explorer.is_state_new(next_state):
                continue
            logger.debug(f"Found new state {next_state}.")
            explorer.update_head(state, next_state, move)
            if next_state == goal_state:
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
