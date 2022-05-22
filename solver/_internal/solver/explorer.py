from math import sqrt

from .move import Move

class Explorer:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._puzzle_len = len(puzzle)
        self._puzzle_slen = int(sqrt(len(puzzle)))

    def _is_left_border(self, pos):
        return (pos % self._puzzle_slen) == 0
    
    def _is_right_border(self, pos):
        return (pos % self._puzzle_slen) == self._puzzle_slen - 1
    
    def _is_top_border(self, pos):
        return pos < self._puzzle_slen
    
    def _is_bottom_border(self, pos):
        return pos >= self._puzzle_len - self._puzzle_slen
    
    def valid_moves_middle(self, pos):
        return [
            Move(pos - 1, pos), # Left
            Move(pos + 1, pos), # Right
            Move(pos - self._puzzle_slen, pos), # Up
            Move(pos + self._puzzle_slen, pos), # Down
        ]
    
    def all_valid_moves(self, zero_pos):
        valid_moves = []
        
        if self._is_left_border(zero_pos):
            if self._is_top_border(zero_pos):
                valid_moves.extend([Move(1, zero_pos),
                                    Move(self._puzzle_slen, zero_pos)])
            elif self._is_bottom_border(zero_pos):
                valid_moves.extend([
                    Move(self._puzzle_len - 2 * self._puzzle_slen, zero_pos),
                    Move(self._puzzle_len - self._puzzle_slen + 1, zero_pos)])
            else:
                valid_moves.extend(valid_moves_middle(zero_pos))
        elif self._is_right_border(zero_pos):
            if self._is_top_border(zero_pos):
                valid_moves.extend([Move(self._puzzle_slen - 2, zero_pos),
                                    Move(self._puzzle_slen * 2 - 1, zero_pos)])
            elif self._is_bottom_border(zero_pos):
                valid_moves.extend([
                    Move(self._puzzle_len - 2, zero_pos),
                    Move(self._puzzle_len - self._puzzle_slen - 1, zero_pos)])
            else:
                valid_moves.extend(valid_moves_middle(zero_pos))
                
        return valid_moves
