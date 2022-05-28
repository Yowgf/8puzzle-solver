from ..utils.utils import slen

def displaced_pieces(state):
    heuristic = 0
    for idx in range(len(state)):
        val = state[idx]
        if val == 0:
            goal_position = len(state) - 1
        else:
            goal_position = val - 1
        if idx != goal_position:
            heuristic += 1
    return heuristic

def _vertical_distance(origin, dest, state_slen):
    # Disconsider horizontal distance
    origin_y = origin // state_slen
    dest_y = dest // state_slen
    return abs(dest_y - origin_y)

def _horizontal_distance(origin, dest, state_slen):
    # Disconsider vertical distance
    origin_h = origin % state_slen
    dest_h = dest % state_slen
    return abs(dest_h - origin_h)

def manhattan_distance(state):
    heuristic = 0
    for idx in range(len(state)):
        val = state[idx]
        if val == 0:
            goal = len(state) - 1
        else:
            goal = val - 1

        state_slen = slen(state)
        
        horizontal_distance = _horizontal_distance(idx, goal, state_slen)
        vertical_distance = _vertical_distance(idx, goal, state_slen)
            
        distance_from_goal = horizontal_distance + vertical_distance

        heuristic += distance_from_goal

    return heuristic
