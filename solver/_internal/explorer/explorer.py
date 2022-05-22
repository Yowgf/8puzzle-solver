from copy import copy
from math import sqrt

from .move import Move
from ..utils.utils import list_mutation

class Explorer:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._puzzle_len = len(puzzle)
        self._puzzle_slen = int(sqrt(len(puzzle)))

    def branch(self):
        valid_moves = self._all_valid_moves(self._puzzle.index(0))
        valid_states = self._get_valid_states(valid_moves)
        return valid_states

    def _is_left_border(self, pos):
        return (pos % self._puzzle_slen) == 0
    
    def _is_right_border(self, pos):
        return (pos % self._puzzle_slen) == self._puzzle_slen - 1
    
    def _is_top_border(self, pos):
        return pos < self._puzzle_slen
    
    def _is_bottom_border(self, pos):
        return pos >= self._puzzle_len - self._puzzle_slen
    
    def _all_valid_moves(self, pos):
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

    def _get_valid_states(self, valid_moves):
        valid_states = []
        for move in valid_moves:
            moved_state = list_mutation(self._puzzle, move.from_pos, move.to_pos)
            valid_states.append(moved_state)
        return valid_states
