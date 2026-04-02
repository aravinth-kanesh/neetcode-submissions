class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array to return - 0 if no future warmer day found
        res = [0] * len(temperatures)
        # monotonically increasing stack storing indices of
        # "unprocessed" days
        stack = []

        # need to access index as well so use enumerate
        for i, temp in enumerate(temperatures):
            # see if warmer day found compared to most recent
            # "unprocessed" day
            # while loop since current day temp could be the "future day"
            # for many previous days
            while stack and temp > temperatures[stack[-1]]:
                # find difference between indices
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return res