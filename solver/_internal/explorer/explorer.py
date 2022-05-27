from random import randint

from ..log import log
from .move import Move
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
            self._head_hash: (state_hash(initial_state), None),
        }

    def is_state_new(self, state):
        stateh = state_hash(state)
        if stateh in self._explored_states:
            return False
        logger.debug(f"State is new: {state}.")
        return True

    # The way we update the head is left to the users of the class. In this
    # fashion, the algorithm being run is transparent to the Explorer.
    def update_head(self, parent_state, child_state, move):
        child_state_hash = state_hash(child_state)
        self._explored_states[child_state_hash] = (
            state_hash(parent_state), move)
        self._head = child_state
        self._head_hash = child_state_hash

    def branch(self):
        return Move.moves_from(self._head)

    def steps_to_cur_state(self):
        initial_state_hash = state_hash(self._initial_state)
        head = self._explored_states[self._head_hash]

        steps = [self._head]
        while head[0] != initial_state_hash:
            steps = [inverse_state_hash(head[0])] + steps
            head = self._explored_states[head[0]]
        if steps != [self._initial_state]:
            steps = [self._initial_state] + steps

        return steps

    def update_head_and_branch(self, state, move):
        state_new = True

        next_state = move.mutate(state)
        if not self.is_state_new(next_state):
            state_new = False
            return None, None, state_new

        self.update_head(state, next_state, move)
        next_moves = self.branch()

        return next_state, next_moves, state_new
