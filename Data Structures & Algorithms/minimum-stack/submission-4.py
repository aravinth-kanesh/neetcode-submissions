class MinStack:
    def __init__(self):
        # stores (val, min_val) tuple
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_val = self.getMin()
            self.stack.append((val, min(val, min_val)))

    def pop(self) -> None:
        # don't need to check for empty stack edge-case
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
