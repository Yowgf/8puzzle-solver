from datetime import datetime

from _internal.config.config import (config_option_mode_breadth_first,
                                     config_option_mode_iterative_deepening,
                                     config_option_mode_uniform_cost,
                                     config_option_mode_astar,
                                     config_option_mode_greedy,
                                     config_option_mode_hill_climbing)
from _internal.policies.bfs import bfs
from _internal.log import log

logger = log.logger()

mode_to_policy = {
    config_option_mode_breadth_first: bfs,
    config_option_mode_iterative_deepening: None,
    config_option_mode_uniform_cost: None,
    config_option_mode_astar: None,
    config_option_mode_greedy: None,
    config_option_mode_hill_climbing: None,
}

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
        initial_state = self._puzzle_entries
        goal_state = self._get_goal()

        mode = self._config.mode
        policy = mode_to_policy[mode]

        policy(initial_state, goal_state)

    def _get_goal(self):
        goal = []
        for i in range(1, len(self._puzzle_entries)):
            goal.append(i)
        # 0 is the empty slot in the puzzle
        goal.append(0)
        return goal
