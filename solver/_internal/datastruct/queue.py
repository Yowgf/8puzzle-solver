class Queue:
    def __init__(self):
        self._l = []

    def __len__(self):
        return len(self._l)

    def push(self, item):
        return self._l.append(item)

    def pop(self):
        return self._l.pop(0)
