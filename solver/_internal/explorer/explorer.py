from random import randint

from ..log import log
from .expansion import Expansion
from .move import Move
from .state import State
from .statistics import Statistics
from ..utils.utils import slen
from ..utils.state import state_hash
from ..utils.state import inverse_state_hash

logger = log.logger()

class Explorer:
    def __init__(self, initial_state):
        self._initial_state = initial_state

        # Map state hash -> State object
        self._explored_states = {}
        self.register_state(initial_state, None, None)

    def is_state_new(self, state):
        stateh = state_hash(state)
        if stateh in self._explored_states:
            return False
        logger.debug(f"State is new: {state}.")
        return True

    def state_depth(self, state):
        stateh = state_hash(state)
        return self._explored_states[stateh].depth

    def register_state(self, state, parent_state, move):
        stateh = state_hash(state)
        if parent_state == None:
            self._explored_states[stateh] = State(stateh, move, 0)
            return

        parent_stateh = state_hash(parent_state)
        ps = self._explored_states[parent_stateh]
        self._explored_states[stateh] = State(parent_stateh, move, ps.depth+1)

    def expand(self, parent_state, move):
        state_new = True

        child_state = move.mutate(parent_state)
        if not self.is_state_new(child_state):
            state_new = False
            return None, state_new

        self.register_state(child_state, parent_state, move)
        next_moves = Move.moves_from(child_state)

        return Expansion(child_state, next_moves), state_new

    def statistics(self):
        return Statistics(num_expanded_states=len(self._explored_states))

    def steps_to_state(self, state):
        stateh = state_hash(state)

        initial_state_hash = state_hash(self._initial_state)
        head = self._explored_states[stateh]

        steps = [state]
        while head.parent_id != initial_state_hash:
            steps = [inverse_state_hash(head.parent_id)] + steps
            head = self._explored_states[head.parent_id]
        if steps != [self._initial_state]:
            steps = [self._initial_state] + steps

        return steps
