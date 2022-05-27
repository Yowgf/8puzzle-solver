# Expansion is a pair (state, move). The idea is to keep track of a branching
# operation in a tree. For example
#
#       0
#     /  \ -- expansion of vertex 0
#    1   2
#
# Here, we would create Expansion(0, [Move(0, 1), Move(0, 1)]) or something like
# that to represent this expansion.
class Expansion:
    def __init__(self, parent_state, moves):
        self.parent_state = parent_state
        self.moves = moves
