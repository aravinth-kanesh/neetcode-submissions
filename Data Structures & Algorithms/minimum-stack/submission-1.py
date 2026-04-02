# the problem with using a standard stack for this problem is that we
# cannot extract the minimum of the stack in constant time complexity

# whenever pushing or popping, need to update the min val accordingly

# idea - when pushing to the stack, push current min val along with val

class MinStack:
    def __init__(self):
        # initialise the stack
        # don't need a min val var: will store alongside each elem
        # min val can be extracted in O(1) time by checking top elem
        self.stack = []
        
    def push(self, val: int) -> None:
        # access last elem on array - corresponds to end of array
        # update min val accordingly
        # no need to return anything
        if self.stack:
            minVal = min(self.stack[-1][1], val)
        else:
            minVal = val

        self.stack.append((val, minVal))

    def pop(self) -> None:
        # popping from our stack returns a tuple
        # only want first element of tuple
        val, minVal = self.stack.pop()
        return val

    def top(self) -> int:
        # only want to return val and not min val
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        # only want to return min val and not val
        return self.stack[-1][1]
        
