from ..._internal.policies.bfs import bfs

class TestBfs:
    def test_bfs_trivial(self, goal_state):
        solution = bfs(goal_state, goal_state)
        assert len(solution) == 1

    def test_bfs_almost_trivial(self, ordered_puzzles, goal_state):
        solution = bfs(ordered_puzzles[-2], goal_state)
        assert len(solution) == 2
        solution = bfs(ordered_puzzles[-3], goal_state)
        assert len(solution) == 3

    def test_bfs_complete(self, real_puzzles, goal_state):
        # Run 10 hardest tests and see if bfs at least finds a solution
        puzzles_to_test = real_puzzles
        for i in range(len(puzzles_to_test)):
            puzzle = puzzles_to_test[i]
            solution = bfs(puzzle, goal_state)
            assert solution != None
            assert len(solution) >= i
