# we will use a stack to store the index of "unprocessed" days
# when iterating through the temperatures, check if is warmer than the
# unprocessed temperatures
# whilst the current temperature is greater than the ones in the stack,
# pop and calculate difference in days
# need to use enumerate to track index and temperature in the same loop
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return res