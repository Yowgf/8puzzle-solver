from ..config.config import (config_option_mode_breadth_first,
                             config_option_mode_iterative_deepening,
                             config_option_mode_uniform_cost,
                             config_option_mode_astar,
                             config_option_mode_greedy,
                             config_option_mode_hill_climbing)
from .bfs import bfs
from .ids import ids
from .dijkstra import dijkstra
from .astar import astar
from .greedy import greedy
from .hclimb import hclimb

class ExpectedAttributes:
    def __init__(self, policyFunc, complete, optimal):
        self.policyFunc = policyFunc
        self.complete   = complete
        self.optimal    = optimal

MODE_TO_POLICY = {
    config_option_mode_breadth_first:       bfs,
    config_option_mode_iterative_deepening: ids,
    config_option_mode_uniform_cost:        dijkstra,
    config_option_mode_astar:               astar,
    config_option_mode_greedy:              greedy,
    config_option_mode_hill_climbing:       hclimb,
}

EXPECTED_POLICY_ATTRIBUTES = {
    config_option_mode_breadth_first:       ExpectedAttributes(bfs, True, False),
    config_option_mode_iterative_deepening: ExpectedAttributes(ids, True, False),
    config_option_mode_uniform_cost:        ExpectedAttributes(dijkstra, True, True),
    config_option_mode_astar:               ExpectedAttributes(astar, True, True),
    config_option_mode_greedy:              ExpectedAttributes(greedy, False, False),
    config_option_mode_hill_climbing:       ExpectedAttributes(hclimb, False, False),
}
