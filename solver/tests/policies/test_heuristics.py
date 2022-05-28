from ..._internal.policies.heuristics import displaced_pieces
from ..._internal.policies.heuristics import manhattan_distance

class TestHeuristics:
    def test_dispacled_pieces_ordered_puzzle(self, ordered_puzzle):
        assert displaced_pieces(ordered_puzzle) == 9

    def test_dispacled_pieces_goal_state(self, goal_state):
        assert displaced_pieces(goal_state) == 0

    def test_manhattan_distance_ordered_puzzle(self, ordered_puzzle):
        # 16 = 4 + 1 + 1 + 3 + 1 + 1 + 3 + 1 + 1
        #      0   1   2   3   4   5   6   7   8
        assert manhattan_distance(ordered_puzzle) == 16

    def test_manhattan_distance_goal_state(self, goal_state):
        assert manhattan_distance(goal_state) == 0
