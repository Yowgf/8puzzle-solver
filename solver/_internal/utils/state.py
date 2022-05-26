def state_hash(state):
    sticked = 0
    for i in range(len(state)):
        sticked += (10 ** i) * state[i]
    return sticked

def inverse_state_hash(h):
    state = []
    s = 0
    i = 1
    while s < h:
        s = (h % (10 ** i))
        digit = s // (10 ** (i - 1))
        state.append(digit)
        i += 1
    if i < 10:
        state.append(0)
    return state
