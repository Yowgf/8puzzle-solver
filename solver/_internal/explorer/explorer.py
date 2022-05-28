from random import randint

from ..log import log
from .expansion import Expansion
from .move import Move
from .state import State
from ..utils.utils import slen
from ..utils.state import state_hash
from ..utils.state import inverse_state_hash

logger = log.logger()

class Explorer:
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self._head = initial_state
        self._head_hash = state_hash(initial_state)

        # Map state hash -> (parent, movement)
        self._explored_states = {
            self._head_hash: State(state_hash(initial_state), None, 0),
        }

    def is_state_new(self, state):
        stateh = state_hash(state)
        if stateh in self._explored_states:
            return False
        logger.debug(f"State is new: {state}.")
        return True

    def state_depth(self, state):
        stateh = state_hash(state)
        assert stateh in self._explored_states
        return self._explored_states[stateh].depth

    # The way we update the head is left to the users of the class. In this
    # fashion, the algorithm being run is transparent to the Explorer.
    def update_head(self, parent_state, child_state, move):
        child_state_hash = state_hash(child_state)
        self._explored_states[child_state_hash] = State(
            state_hash(parent_state), move, 0)
        self._head = child_state
        self._head_hash = child_state_hash

    def branch(self):
        return Move.moves_from(self._head)

    def update_head_and_branch(self, parent_state, move):
        state_new = True

        child_state = move.mutate(parent_state)
        if not self.is_state_new(child_state):
            state_new = False
            return None, state_new

        self.update_head(parent_state, child_state, move)
        next_moves = self.branch()

        return Expansion(child_state, next_moves), state_new

    def steps_to_cur_state(self):
        initial_state_hash = state_hash(self._initial_state)
        head = self._explored_states[self._head_hash]

        steps = [self._head]
        while head.parent_id != initial_state_hash:
            steps = [inverse_state_hash(head.parent_id)] + steps
            head = self._explored_states[head.parent_id]
        if steps != [self._initial_state]:
            steps = [self._initial_state] + steps

        return steps
