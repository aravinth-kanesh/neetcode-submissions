class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
