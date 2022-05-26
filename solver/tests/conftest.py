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
def goal_state(ordered_puzzles):
    return ordered_puzzles[-1]

@pytest.fixture
def real_puzzles():
    # Puzzles in order of minimum number of steps to complete it.
    return [
        # 0 steps
        [1, 2, 3,
         4, 5, 6,
         7, 8, 0],
        # 1 steps
        [1, 2, 3,
         4, 5, 6,
         7, 0, 8],
        # 2 steps
        [1, 2, 3,
         4, 0, 5,
         7, 8, 6],
        # 3 steps
        [1, 0, 3,
         4, 2, 5,
         7, 8, 6],
        # 4 steps
        [1, 5, 2,
         4, 0, 3,
         7, 8, 6],
        # 5 steps
        [1, 5, 2,
         0, 4, 3,
         7, 8, 6],
        # 6 steps
        [1, 5, 2,
         4, 8, 3,
         7, 6, 0],
        # 7 steps
        [1, 5, 2,
         4, 8, 0,
         7, 6, 3],
        # 8 steps
        [0, 5, 2,
         1, 8, 3,
         4, 7, 6],
        # 9 steps
        [1, 0, 2,
         8, 5, 3,
         4, 7, 6],
        # 10 steps
        [5, 8, 2,
         1, 0, 3,
         4, 7, 6],
    ]
