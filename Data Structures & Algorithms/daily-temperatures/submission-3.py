class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # push "unprocessed" indexes of temperatures to the stack
        stack = []

        # number of days
        n = len(temperatures)

        # final array
        result = [0] * n
        
        for i, temp in enumerate(temperatures):
            while i > 0 and stack and temp > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                # that day has been processed
                stack.pop()

            # push unprocessed day to the stack
            stack.append(i)

        return result