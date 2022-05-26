import pytest

from ..._internal.utils.state import inverse_state_hash
from ..._internal.utils.state import state_hash

class TestState:
    def test_state_hash_0(self, ordered_puzzles):
        assert 876543210 == state_hash(ordered_puzzles[0])

    def test_state_hash_1(self, ordered_puzzles):
        assert 876543201 == state_hash(ordered_puzzles[1])

    def test_state_hash_2(self, ordered_puzzles):
        assert 876543021 == state_hash(ordered_puzzles[2])

    def test_state_hash_3(self, ordered_puzzles):
        assert 876540321 == state_hash(ordered_puzzles[3])

    def test_state_hash_4(self, ordered_puzzles):
        assert 876504321 == state_hash(ordered_puzzles[4])

    def test_state_hash_5(self, ordered_puzzles):
        assert 876054321 == state_hash(ordered_puzzles[5])

    def test_state_hash_6(self, ordered_puzzles):
        assert 870654321 == state_hash(ordered_puzzles[6])

    def test_state_hash_7(self, ordered_puzzles):
        assert 807654321 == state_hash(ordered_puzzles[7])

    def test_state_hash_8(self, ordered_puzzles):
        assert 87654321 == state_hash(ordered_puzzles[8])

    def test_inverse_state_hash_invertible(self, ordered_puzzles):
        for puzzle in ordered_puzzles:
            assert puzzle == inverse_state_hash(state_hash(puzzle))
