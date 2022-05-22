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
        return 
    
    def all_valid_moves(self, pos):
        valid_moves = []
        
        if self._is_left_border(pos):
            if self._is_top_border(pos):
                valid_moves.extend([Move(1, pos),
                                    Move(self._puzzle_slen, pos)])
            elif self._is_bottom_border(pos):
                valid_moves.extend([
                    Move(self._puzzle_len - 2 * self._puzzle_slen, pos),
                    Move(self._puzzle_len - self._puzzle_slen + 1, pos)])
            else:
                valid_moves.extend([
                    Move(pos - self._puzzle_slen, pos),
                    Move(pos + 1, pos),
                    Move(pos + self._puzzle_slen, pos)])
        elif self._is_right_border(pos):
            if self._is_top_border(pos):
                valid_moves.extend([Move(self._puzzle_slen - 2, pos),
                                    Move(self._puzzle_slen * 2 - 1, pos)])
            elif self._is_bottom_border(pos):
                valid_moves.extend([
                    Move(self._puzzle_len - 2, pos),
                    Move(self._puzzle_len - self._puzzle_slen - 1, pos)])
            else:
                valid_moves.extend([
                    Move(pos - self._puzzle_slen, pos),
                    Move(pos - 1, pos),
                    Move(pos + self._puzzle_slen, pos)])
        elif self._is_top_border(pos):
                valid_moves.extend([
                    Move(pos - 1, pos),
                    Move(pos + 1, pos),
                    Move(pos + self._puzzle_slen, pos)])
        elif self._is_bottom_border(pos):
                valid_moves.extend([
                    Move(pos - 1, pos),
                    Move(pos + 1, pos),
                    Move(pos - self._puzzle_slen, pos)])
        # Middle
        else:
            valid_moves.extend([
                Move(pos - 1, pos),
                Move(pos + 1, pos),
                Move(pos - self._puzzle_slen, pos),
                Move(pos + self._puzzle_slen, pos)])

        return valid_moves
