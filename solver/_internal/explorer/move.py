from ..utils.utils import slen
from ..utils.utils import swap

class Move:
    def __init__(self, from_pos, to_pos):
        self.from_pos = from_pos
        self.to_pos = to_pos

    def mutate(self, l):
        return swap(l, self.from_pos, self.to_pos)
    
    def moves_from(origin):
        moves = []

        pos = origin.index(0)
        origin_len = len(origin)
        origin_slen = slen(origin)
        
        if Move._is_left_border(pos, origin_slen):
            if Move._is_top_border(pos, origin_slen):
                moves.extend([Move(1, pos),
                                    Move(origin_slen, pos)])
            elif Move._is_bottom_border(pos, origin_len, origin_slen):
                moves.extend([
                    Move(origin_len - 2 * origin_slen, pos),
                    Move(origin_len - origin_slen + 1, pos)])
            else:
                moves.extend([
                    Move(pos - origin_slen, pos),
                    Move(pos + 1, pos),
                    Move(pos + origin_slen, pos)])
        elif Move._is_right_border(pos, origin_slen):
            if Move._is_top_border(pos, origin_slen):
                moves.extend([Move(origin_slen - 2, pos),
                                    Move(origin_slen * 2 - 1, pos)])
            elif Move._is_bottom_border(pos, origin_len, origin_slen):
                moves.extend([
                    Move(origin_len - 2, pos),
                    Move(origin_len - origin_slen - 1, pos)])
            else:
                moves.extend([
                    Move(pos - origin_slen, pos),
                    Move(pos - 1, pos),
                    Move(pos + origin_slen, pos)])
        elif Move._is_top_border(pos, origin_slen):
                moves.extend([
                    Move(pos - 1, pos),
                    Move(pos + 1, pos),
                    Move(pos + origin_slen, pos)])
        elif Move._is_bottom_border(pos, origin_len, origin_slen):
                moves.extend([
                    Move(pos - 1, pos),
                    Move(pos + 1, pos),
                    Move(pos - origin_slen, pos)])
        # Middle
        else:
            moves.extend([
                Move(pos - 1, pos),
                Move(pos + 1, pos),
                Move(pos - origin_slen, pos),
                Move(pos + origin_slen, pos)])

        return moves

    def _is_left_border(pos, origin_slen):
        return (pos % origin_slen) == 0
    
    def _is_right_border(pos, origin_slen):
        return (pos % origin_slen) == origin_slen - 1
    
    def _is_top_border(pos, origin_slen):
        return pos < origin_slen
    
    def _is_bottom_border(pos, origin_len, origin_slen):
        return pos >= origin_len - origin_slen
