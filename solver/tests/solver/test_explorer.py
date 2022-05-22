import pytest

from ..._internal.solver.explorer import Explorer
from ..._internal.solver.move import Move

class TestSolverExplorer:
    @pytest.fixture
    def dummy_puzzle(self):
        return [
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        ]

    def moves_equal(self, moves1, moves2):
        for (move1, move2) in zip(moves1, moves2):
            assert move1.from_pos == move2.from_pos
            assert move1.to_pos == move2.to_pos

    def test_all_valid_moves_upperleft(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(0),
                         [Move(1, 0), Move(3, 0)])
