from random import randint

from ..log import log
from .move import Move
from ..utils.utils import slen

logger = log.logger()

MAX_NUMBER_EXPLORED_STATES = 10_000_000

class Explorer:
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self._head = initial_state
        self._head_hash = self._state_hash(initial_state)

        # Map state hash -> (parent, movement)
        self._explored_states = {
            self._head_hash: (self._state_hash(initial_state), None),
        }

    def is_state_new(self, state):
        state_hash = self._state_hash(state)
        if state_hash in self._explored_states:
            return False
        return True

    # The way we update the head is left to the users of the class. In this
    # fashion, the algorithm being run is transparent to the Explorer.
    def update_head(self, parent_state, child_state, move):
        child_state_hash = self._state_hash(child_state)
        self._explored_states[child_state_hash] = (self._state_hash(parent_state),
                                                   move)
        self._head = child_state
        self._head_hash = child_state_hash

    def branch(self):
        return Move.moves_from(self._head)

    def steps_to_cur_state(self):
        initial_state_hash = self._state_hash(self._initial_state)
        head = self._explored_states[self._head_hash]
        steps = [self._head]
        while head[0] != initial_state_hash:
            steps = [self._inverse_state_hash(head[0])] + steps
            head = self._explored_states[head[0]]
        if steps != [self._initial_state]:
            steps = [self._initial_state] + steps

        return steps

    def _inverse_state_hash(self, h):
        state = []
        s = 0
        i = 1
        while s < h:
            s = (h % (10 ** i))
            digit = s // (10 ** (i - 1))
            state.append(digit)
            i += 1
        if len(state) < len(self._initial_state):
            state.append(0)
        return state

    def _state_hash(self, state):
        sticked = 0
        for i in range(len(state)):
            sticked += (10 ** i) * state[i]
        return sticked

    def _get_valid_states(self, valid_moves):
        valid_states = []
        for move in valid_moves:
            moved_state = move.mutate(self._head)
            valid_states.append(moved_state)
        return valid_states
