class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        self.stack.append([val, min(min_val, val)])

    def pop(self) -> None:
        popped = self.stack[-1][0]
        self.stack.pop()
        return popped

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return float('inf')
        return self.stack[-1][1]
