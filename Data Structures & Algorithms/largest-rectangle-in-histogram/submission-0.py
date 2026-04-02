class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max area is initially 0
        maxArea = 0
        stack = [] # stores a pair - (start, height)

        for i, h in enumerate(heights):
            # start index is at current one for now
            start = i
            # bars which are taller than the current must stop here
            # compute area of bar and pop from stack
            # extend current bar to the left
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            # add the current bar to the stack
            stack.append((start, h))

        # there could be unprocessed bars still left over in the stack
        # after looping through all the bars
        # compute areas of those rectangles and see if max area gets
        # updated
        # all of these remaining bars extend to the end of the hist
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

