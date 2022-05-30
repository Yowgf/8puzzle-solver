from ..._internal.policies.bfs import bfs
from ..._internal.explorer.explorer import Explorer
from ..._internal.explorer.move import Move

class TestExplorer:
    def test_state_depth_initial_state(self, ordered_puzzle):
        explorer = Explorer(ordered_puzzle)
        assert explorer.state_depth(ordered_puzzle) == 0

    def test_state_depth_depth2(self, ordered_puzzles, goal_state):
        initial_state = ordered_puzzles[-3]
        explorer = Explorer(initial_state)
        solution, _ = bfs(initial_state, goal_state, test_explorer=explorer)
        assert len(solution) == 3
        assert explorer.state_depth(goal_state) == 2
