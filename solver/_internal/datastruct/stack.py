class Stack:
    def __init__(self):
        self._l = []

    def __len__(self):
        return len(self._l)

    def push(self, n):
        return self._l.append(n)

    def pop(self):
        return self._l.pop()
