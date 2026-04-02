class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.stack[-1][1] if self.stack else float('infinity')
        min_val = min(min_val, val)
        self.stack.append((val, min_val))

    def pop(self) -> None:
        val, min_val = self.stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
