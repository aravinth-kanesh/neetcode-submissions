class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        # to store indexes of days not "processed" yet
        stack = []

        # need to track indexes as well - use enumerate
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                # find the difference in days using indexes
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            # otherwise append to the stack to be processed later
            stack.append(i)

        # days where there is no future day with a warmer temp will
        # default to 0 as how the result array was instantiated
        return result