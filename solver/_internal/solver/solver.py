from datetime import datetime

from _internal.log import log
from _internal.policies.policies import MODE_TO_POLICY
from _internal.utils.utils import slen

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
        initial_state = self._puzzle_entries
        goal_state = self._get_goal()

        mode = self._config.mode
        policy = MODE_TO_POLICY[mode]

        steps_to_goal, statistics = policy(initial_state, goal_state)
        logger.debug(f"Steps to goal: {steps_to_goal}")
        self._print_num_steps(steps_to_goal)
        if self._config.print_statistics:
            self._print_statistics(statistics)
        if self._config.print_result:
            self._print_result(steps_to_goal)

    def _get_goal(self):
        goal = []
        for i in range(1, len(self._puzzle_entries)):
            goal.append(i)
        # 0 is the empty slot in the puzzle
        goal.append(0)
        return goal

    def _print_num_steps(self, steps_to_goal):
        if steps_to_goal == None:
            print("Solution not found.")
            return

        print(f"{len(steps_to_goal)-1}", end="\n\n")

    def _print_statistics(self, statistics):
        print("{"+
              f'"num_expanded_states": {statistics.num_expanded_states}'+
              "}")

    def _print_result(self, steps_to_goal):
        if steps_to_goal == None:
            return

        puzzle_slen = slen(self._puzzle_entries)

        for step in steps_to_goal:
            i = 0
            while i < puzzle_slen:
                j = 0
                while j < puzzle_slen:
                    print(step[i * puzzle_slen + j], end=" ")
                    j += 1
                print("")
                i += 1
            print("")
