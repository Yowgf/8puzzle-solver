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
        self._explored_states[child_state_hash] = (self._head_hash, move)
        self._head = child_state
        self._head_hash = child_state_hash

    def branch(self):
        return Move.moves_from(self._head)

    def steps_to_cur_state(self):
        moves = []
        hash_path = []
        initial_state_hash = self._state_hash(self._initial_state)
        head = self._explored_states[self._head_hash]
        while head[0] != initial_state_hash:
            moves = [head[1]] + moves
            head = self._explored_states[head[0]]

        steps = [self._initial_state]
        head = self._initial_state
        for move in moves:
            new_head = move.mutate(head)
            steps.append(new_head)
            head = new_head
        return steps

    def _state_hash(self, state):
        m = max(state) + 2
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
