from ..config.config import (
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
)

# Policies
from .bfs import bfs
from .ids import ids
from .dijkstra import dijkstra
from .astar import astar
from .greedy import greedy
from .hclimb import hclimb
# Heuristics
from .heuristics import manhattan_distance
from .heuristics import displaced_pieces

class ExpectedAttributes:
    def __init__(self, policyFunc, complete, optimal):
        self.policyFunc = policyFunc
        self.complete   = complete
        self.optimal    = optimal

MODE_TO_POLICY = {
    # Required
    config_option_mode_breadth_first:       bfs,
    config_option_mode_iterative_deepening: ids,
    config_option_mode_uniform_cost:        dijkstra,
    config_option_mode_astar:               astar,
    config_option_mode_greedy:              greedy,
    config_option_mode_hill_climbing:       hclimb,

    # Additional
    config_option_mode_astar_manhattan: lambda a, b: astar(a, b, manhattan_distance),
    config_option_mode_astar_displaced: lambda a, b: astar(a, b, displaced_pieces),
    config_option_mode_greedy_manhattan: lambda a, b: greedy(a, b, manhattan_distance),
    config_option_mode_greedy_displaced: lambda a, b: greedy(a, b, displaced_pieces),
}

EXPECTED_POLICY_ATTRIBUTES = {
    config_option_mode_breadth_first:       ExpectedAttributes(bfs, True, False),
    config_option_mode_iterative_deepening: ExpectedAttributes(ids, True, False),
    config_option_mode_uniform_cost:        ExpectedAttributes(dijkstra, True, True),
    config_option_mode_astar:               ExpectedAttributes(astar, True, True),
    config_option_mode_greedy:              ExpectedAttributes(greedy, False, False),
    config_option_mode_hill_climbing:       ExpectedAttributes(hclimb, False, False),
}
