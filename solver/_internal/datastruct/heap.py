import heapq

class Heap:
    def __init__(self):
        self._l = []

    def pop(self):
        return heapq.heappop(self._l)

    def push(self, item):
        return heapq.heappush(self._l, item)
