import sys

from _internal.config.config import InvalidConfigError
from _internal.config.config import parse_config
from _internal.config.config import print_usage
from _internal.log import log
from _internal.solver.solver import Solver
from _internal.utils.utils import solver_run_result
from _internal.utils.utils import STATUS_FAILED
from _internal.utils.utils import STATUS_SUCCESS

logger = log.logger()

def main():
    success_message = ""

    try:
        try:
            cfg = parse_config(sys.argv[1:])
        except InvalidConfigError as e:
            print_usage(e)
            return solver_run_result(status=STATUS_FAILED,
                                     reason=f"Invalid config: {e}")

        logger.info(
            "Successfully parsed config. Config in json format:\n" + cfg.to_json()
        )

        logger.info("Initializing solver.")

        solver = Solver(cfg)
        solver.init()

        logger.info("Successfully initialized solver.")

        logger.info("Starting solver run.")

        success_message = solver.run_timed()

        logger.info("Solver ran successfully.")

        return solver_run_result(status=STATUS_SUCCESS, reason=success_message)

    except Exception as e:
        logger.critical(e, exc_info=True)

        return solver_run_result(status=STATUS_FAILED,
                                 reason=f"Solver run failed: {e}")

if __name__ == '__main__':
    main()
