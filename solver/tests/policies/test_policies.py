import pytest

from ..._internal.policies.policies import EXPECTED_POLICY_ATTRIBUTES

class TestPolicies:
    def test_trivial(self, goal_state):
        for policy_name in EXPECTED_POLICY_ATTRIBUTES:
            policy = EXPECTED_POLICY_ATTRIBUTES[policy_name]
            # TODO: remove this check when all policies are implemented.
            if policy == None:
                continue
            solution, _ = policy.policyFunc(goal_state, goal_state)
            assert len(solution) == 1, policy_name

    def test_almost_trivial(self, ordered_puzzles, goal_state):
        for policy_name in EXPECTED_POLICY_ATTRIBUTES:
            policy = EXPECTED_POLICY_ATTRIBUTES[policy_name]
            # TODO: remove this check when all policies are implemented.
            if policy == None:
                continue

            solution, _ = policy.policyFunc(ordered_puzzles[-2], goal_state)
            assert len(solution) == 2, policy_name
            solution, _ = policy.policyFunc(ordered_puzzles[-3], goal_state)
            assert len(solution) == 3, policy_name
            
    def test_real(self, real_puzzles, goal_state):
        for policy_name in EXPECTED_POLICY_ATTRIBUTES:
            policy = EXPECTED_POLICY_ATTRIBUTES[policy_name]
            # TODO: remove this check when all policies are implemented.
            if policy == None:
                continue
            if not policy.complete:
                continue

            # Check if policy at least finds a valid solution for each puzzle
            puzzles_to_test = real_puzzles
            for i in range(len(puzzles_to_test)):
                puzzle = puzzles_to_test[i]
                solution, _ = policy.policyFunc(puzzle, goal_state)
                assert solution != None, policy_name
                if policy.optimal:
                    assert len(solution)-1 == i, policy_name
                else:
                    assert len(solution) >= i, policy_name
