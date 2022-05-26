from .._internal.utils.utils import swap

def move_empty_spot(l, num_positions):
    for i in range(num_positions):
        l = swap(l, i, i+1)
    return l
