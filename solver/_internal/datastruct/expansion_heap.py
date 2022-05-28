import heapq

class ExpansionHeap:
    def __init__(self):
        self._l = []

    def __len__(self):
        return len(self._l)

    def pop(self):
        return heapq.heappop(self._l)

    # Order by depth
    def push(self, depth, expansion):
        return heapq.heappush(self._l, (depth, expansion))
