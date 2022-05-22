from random import randint

from ..log import log
from .move import Move
from ..utils.utils import list_mutation
from ..utils.utils import slen

logger = log.logger()

MAX_NUMBER_EXPLORED_STATES = 10_000_000

class Node:
    def __init__(self, nodeid, left_child=None, right_child=None, data=None):
        self.nodeid = nodeid
        self.left_child = left_child
        self.right_child = right_child
        self.data = data

    def insert(self, nodeid, data):
        if nodeid < self.nodeid:
            if self.left_child == None:
                self.left_child = Node(nodeid, None, None, data)
            else:
                self.left_child.insert(nodeid, data)
        elif nodeid > self.nodeid:
            if self.right_child == None:
                self.right_child = Node(nodeid, None, None, data)
            else:
                self.right_child.insert(nodeid, data)
        elif nodeid == self.nodeid:
            self.data = data
        else:
            raise RuntimeError("Nodeid passed to Node.insert is really weird!")

    # path_to returns a list of all nodes that need to be traversed until we get
    # to the given node.
    def path_to(self, nodeid, path):
        path.append(self)
        if nodeid == self.nodeid:
            return
        elif nodeid < self.nodeid:
            if self.left_child == None:
                raise RuntimeError(f"Cannot find given node id. nodeid={nodeid} "+
                                   f"path={path}. Failed in left child.")
            else:
                return self.left_child.path_to(nodeid, path)
        elif nodeid > self.nodeid:
            if self.right_child == None:
                raise RuntimeError(f"Cannot find given node id. nodeid={nodeid} "+
                                   f"path={path}. Failed in right child.")
            else:
                return self.right_child.path_to(nodeid, path)
        else:
            raise RuntimeError("Nodeid passed to Node.path_to is really weird! "+
                               f"nodeid={nodeid} path={path}")

# BST is a binary search tree.
class BST:
    def __init__(self, root):
        self._root = root
        self._size = 1

    def insert(self, nodeid, data):
        logger.debug(f"Inserting node in BST. "+
                     f"nodeid={nodeid}. Current size: {self._size}")
        self._root.insert(nodeid, data)
        logger.debug(f"Inserted. L={self._root.left_child} R={self._root.right_child}")
        self._size += 1

    def path_to(self, nodeid):
        logger.debug(f"Finding node in BST. nodeid={nodeid} ")
        path = []
        self._root.path_to(nodeid, path)
        return path

class Explorer:
    def __init__(self, initial_state):
        self._head = initial_state
        self._head_len = len(initial_state)
        self._head_slen = slen(initial_state)

        self._nodeid_cache = set()

        # Initialize BST to cache all paths walked through so far.
        self._cur_nodeid = self._new_nodeid()
        root_node = Node(self._cur_nodeid, None, None, initial_state)
        self._bst = BST(root_node)

    # The way we update the head is left to the users of the class. In this
    # fashion, the algorithm being run is transparent to the Explorer.
    def update_head(self, new_head):
        self._head = new_head
        child_nodeid = self._new_nodeid()
        self._bst.insert(child_nodeid, new_head)
        self._cur_nodeid = child_nodeid

    def branch(self):
        valid_moves = self._all_valid_moves(self._head.index(0))
        valid_states = self._get_valid_states(valid_moves)
        return valid_states

    def steps_to_cur_state(self):
        nodes_to_cur_state = self._bst.path_to(self._cur_nodeid)
        steps_to_cur_state = []
        for node in nodes_to_cur_state:
            logger.debug(f"Data: {node.data}")
            steps_to_cur_state.append(node.data)
        return steps_to_cur_state

    def _new_nodeid(self):
        def get_rand():
            # Use 10 time the maximum number, otherwise will be too many
            # conflicts.
            return randint(0, MAX_NUMBER_EXPLORED_STATES * 10)
        new_nodeid = get_rand()
        while new_nodeid in self._nodeid_cache:
            new_nodeid = get_rand()
        self._nodeid_cache.add(new_nodeid)
        return new_nodeid

    def _is_left_border(self, pos):
        return (pos % self._head_slen) == 0
    
    def _is_right_border(self, pos):
        return (pos % self._head_slen) == self._head_slen - 1
    
    def _is_top_border(self, pos):
        return pos < self._head_slen
    
    def _is_bottom_border(self, pos):
        return pos >= self._head_len - self._head_slen
    
    def _all_valid_moves(self, pos):
        valid_moves = []
        
        if self._is_left_border(pos):
            if self._is_top_border(pos):
                valid_moves.extend([Move(1, pos),
                                    Move(self._head_slen, pos)])
            elif self._is_bottom_border(pos):
                valid_moves.extend([
                    Move(self._head_len - 2 * self._head_slen, pos),
                    Move(self._head_len - self._head_slen + 1, pos)])
            else:
                valid_moves.extend([
                    Move(pos - self._head_slen, pos),
                    Move(pos + 1, pos),
                    Move(pos + self._head_slen, pos)])
        elif self._is_right_border(pos):
            if self._is_top_border(pos):
                valid_moves.extend([Move(self._head_slen - 2, pos),
                                    Move(self._head_slen * 2 - 1, pos)])
            elif self._is_bottom_border(pos):
                valid_moves.extend([
                    Move(self._head_len - 2, pos),
                    Move(self._head_len - self._head_slen - 1, pos)])
            else:
                valid_moves.extend([
                    Move(pos - self._head_slen, pos),
                    Move(pos - 1, pos),
                    Move(pos + self._head_slen, pos)])
        elif self._is_top_border(pos):
                valid_moves.extend([
                    Move(pos - 1, pos),
                    Move(pos + 1, pos),
                    Move(pos + self._head_slen, pos)])
        elif self._is_bottom_border(pos):
                valid_moves.extend([
                    Move(pos - 1, pos),
                    Move(pos + 1, pos),
                    Move(pos - self._head_slen, pos)])
        # Middle
        else:
            valid_moves.extend([
                Move(pos - 1, pos),
                Move(pos + 1, pos),
                Move(pos - self._head_slen, pos),
                Move(pos + self._head_slen, pos)])

        return valid_moves

    def _get_valid_states(self, valid_moves):
        valid_states = []
        for move in valid_moves:
            moved_state = list_mutation(self._head, move.from_pos, move.to_pos)
            valid_states.append(moved_state)
        return valid_states
