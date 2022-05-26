import pytest

from ..._internal.explorer.move import Move

class TestMove:
    def moves_equal(self, moves1, moves2):
        for (move1, move2) in zip(moves1, moves2):
            assert move1.from_pos == move2.from_pos
            assert move1.to_pos == move2.to_pos

    def test_moves_from_0(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[0]),
            [Move(1, 0), Move(3, 0)])

    def test_moves_from_1(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[1]),
                         [Move(0, 1), Move(2, 1), Move(4, 1)])

    def test_moves_from_2(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[2]),
            [Move(1, 2), Move(5, 2)])

    def test_moves_from_3(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[3]),
            [Move(0, 3), Move(4, 3), Move(6, 3)])

    def test_moves_from_4(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[4]),
            [Move(3, 4), Move(5, 4), Move(1, 4), Move(7, 4)])

    def test_moves_from_5(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[5]),
            [Move(2, 5), Move(4, 5), Move(8, 5)])

    def test_moves_from_6(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[6]),
            [Move(3, 6), Move(7, 6)])

    def test_moves_from_7(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[7]),
            [Move(6, 7), Move(8, 7), Move(4, 7)])

    def test_moves_from_8(self, ordered_puzzles):
        self.moves_equal(Move.moves_from(ordered_puzzles[8]),
            [Move(7, 8), Move(5, 8)])
