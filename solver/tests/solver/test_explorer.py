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

    def test_all_valid_moves_0(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(0),
                         [Move(1, 0), Move(3, 0)])

    def test_all_valid_moves_1(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(1),
                         [Move(0, 1), Move(2, 1), Move(4, 1)])

    def test_all_valid_moves_2(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(2),
                         [Move(1, 2), Move(5, 2)])

    def test_all_valid_moves_3(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(3),
                         [Move(0, 3), Move(4, 3), Move(6, 3)])

    def test_all_valid_moves_4(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(4),
                         [Move(3, 4), Move(5, 4), Move(1, 4), Move(7, 4)])

    def test_all_valid_moves_5(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(5),
                         [Move(2, 5), Move(4, 5), Move(8, 5)])

    def test_all_valid_moves_6(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(6),
                         [Move(3, 6), Move(7, 6)])

    def test_all_valid_moves_7(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(7),
                         [Move(6, 7), Move(8, 7), Move(4, 7)])

    def test_all_valid_moves_8(self, dummy_puzzle):
        explorer = Explorer(dummy_puzzle)
        self.moves_equal(explorer.all_valid_moves(8),
                         [Move(7, 8), Move(5, 8)])
