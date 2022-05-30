import logging

from ..utils.utils import file_exists
from ..utils.utils import between
from ..log import log
from ..log.log import set_level

logger = log.logger()

# These are the additional modes available so that different heuristics may be
# tested.
config_option_mode_astar_manhattan = 'AM'
config_option_mode_astar_displaced = 'AD'
config_option_mode_greedy_manhattan = 'GM'
config_option_mode_greedy_displaced = 'GD'

# These options are required in the assignment specification.
config_option_mode_breadth_first = 'B'
config_option_mode_iterative_deepening = 'I'
config_option_mode_uniform_cost = 'U'
config_option_mode_astar = 'A'
config_option_mode_greedy = 'G'
config_option_mode_hill_climbing = 'H'
valid_modes = [
    # Required
    config_option_mode_breadth_first,
    config_option_mode_iterative_deepening,
    config_option_mode_uniform_cost,
    config_option_mode_astar,
    config_option_mode_greedy,
    config_option_mode_hill_climbing,

    # Additional
    config_option_mode_astar_manhattan,
    config_option_mode_astar_displaced,
    config_option_mode_greedy_manhattan,
    config_option_mode_greedy_displaced,      
]
config_option_print_result = "PRINT"

# Additional options (not required in the assignment specification)
config_option_debug = '-d'
config_option_log_level = '-log-level'
config_option_print_statistics = 'PRINT_STATISTICS'

class InvalidConfigError(Exception):
    def __init__(self, config_option_key, err_msg):
        super().__init__(
            "invalid value for flag '{}': {}".format(
                config_option_key, err_msg,
            )
        )

class Config:
    puzzle_entries_key = 'puzzle_entries'
    debug_key = 'debug'

    def __init__(self, mode, puzzle_entries, print_result=False, print_statistics=False, debug=False):
        self.mode = mode
        self.puzzle_entries = puzzle_entries
        self.print_result = print_result
        self.print_statistics = print_statistics
        self.debug = debug

    def to_json(self):
        def json_mapping(key, val):
            return f'"{key}": "{val}"'

        return (
            '{\n' +
            json_mapping("mode", self.mode) + ",\n" +
            json_mapping("puzzle_entries", self.puzzle_entries) + ",\n" +
            json_mapping("print_result", self.print_result) + ",\n" +
            json_mapping("print_statistics", self.print_statistics) + ",\n" +
            json_mapping("debug", self.debug) +
            '\n}'
        )

def print_usage(config_error):
    print(f"Invalid config: {config_error}")
    print(
"""
Usage: <solver> <mode> <puzzle entries (9 of them)> [-d]
                [-log-level=<python-like log level string>]"""
)

def get_eqseparated_val(key, s):
    split_by_eq = s.split("=")
    if len(split_by_eq) < 2:
        raise InvalidConfigError(key, f"must be a '='-separated string. "+
                                 f"Got: {s}")
    return split_by_eq[1]

def initialize_log_level(log_level_config_key, log_level):
    try:
        log.set_level(log_level)
    except ValueError as e:
        raise InvalidConfigError(log_level_config_key, e)

def parse_config(args):
    # Must receive exactly this many entries, otherwise config is invalid.
    num_puzzle_entries = 9
    # Start with empty list for entries.
    mode = None
    puzzle_entries = []
    print_result = False
    print_statistics = False

    # Non-required flags
    debug = False
    # Log level set to CRITICAL by default, to avoid outputting things that the
    # assignment grader will find weird.
    log_level = None

    arg_idx = 0
    while arg_idx < len(args):
        arg = args[arg_idx]
        if arg == config_option_debug:
            debug = True
        elif arg.startswith(config_option_log_level):
            log_level = get_eqseparated_val(config_option_log_level, arg)
        elif arg == config_option_print_result:
            print_result = True
        elif arg == config_option_print_statistics:
            print_statistics = True
        elif arg in valid_modes:
            mode = arg
        elif len(puzzle_entries) < num_puzzle_entries:
            try:
                entry = int(arg)
                puzzle_entries.append(entry)
            # If conversion to int didn't work, we just don't include the
            # argument as a puzzle entry.
            except (TypeError, ValueError) as e:
                pass

        arg_idx += 1

    if not mode in valid_modes:
        raise InvalidConfigError(
            "mode",
            f"mode must be one of: {valid_modes}",
        )

    if len(puzzle_entries) != num_puzzle_entries:
        raise InvalidConfigError(
            "puzzle entries",
            f"wrong number of entries: expected {num_puzzle_entries} "+
            f"got {len(puzzle_entries)}",
        )

    if log_level != None:
        initialize_log_level(config_option_log_level, log_level)

    return Config(mode, puzzle_entries, print_result=print_result,
                  print_statistics=print_statistics, debug=debug)
