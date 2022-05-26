import pytest

from .testutils import move_empty_spot

@pytest.fixture
def ordered_puzzle():
    return [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,
    ]

@pytest.fixture
def ordered_puzzles(ordered_puzzle):
    puzzles = []
    for i in range(9):
        puzzles.append(move_empty_spot(ordered_puzzle, i))
    return puzzles

@pytest.fixture
def real_puzzles():
    # Puzzles + minimum number of steps to complete it
    puzzles_solution = {
        [1, 2, 3,
         4, 5, 6,
         7, 8, 0]: 0,
        
    }
