class State:
    # `parent_id` is the ID of the parent state. `move` is the movement from
    # that state that led to this state.
    def __init__(self, parent_id, move, depth):
        self.parent_id = parent_id
        self.move = move
        self.depth = depth
