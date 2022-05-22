from datetime import datetime

from _internal.log import log

logger = log.logger()

class Solver:
    def __init__(self, config):
        self.config = config
        self.puzzle_entries = self.config.puzzle_entries

    def init(self):
        pass

    def run_timed(self):
        before = datetime.now()
        self.run()
        elapsed = datetime.now() - before
        logger.info(f"Elapsed time: {elapsed}")

    # Goal: have block 0 in position 9
    def run(self):
        # Breadth-first search: 
        steps = []
