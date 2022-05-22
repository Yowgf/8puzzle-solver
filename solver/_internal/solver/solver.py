from datetime import datetime

from _internal.explorer.explorer import Explorer
from _internal.log import log

logger = log.logger()

class Solver:
    def __init__(self, config):
        self._config = config
        self._puzzle_entries = config.puzzle_entries

    def init(self):
        pass

    def run_timed(self):
        before = datetime.now()
        self.run()
        elapsed = datetime.now() - before
        logger.info(f"Elapsed time: {elapsed}")

    def run(self):
        # BFS
        #
        # TODO: how to keep track of the steps we are taking?
        goal_state = [1,2,3,4,5,6,7,8,0]
        frontier = [self._puzzle_entries]
        explored = []
        found_goal = False
        while len(frontier) > 0 and not found_goal:
            state = frontier.pop()
            logger.debug(f"Exploring state {state}")
            if state in explored:
                continue
            else:
                explored.append(state)
            if state == goal_state:
                found_goal = True
            explorer = Explorer(state)
            next_states = explorer.branch()
            frontier.extend(next_states)

        if found_goal:
            print("Found goal")
        else:
            print("Did not find goal")
