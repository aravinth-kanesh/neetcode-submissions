class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # completely before the current interval
            # add newInterval and every interval after - already sorted
            # and non-overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # completely after the current interval
            # add the current interval to res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlapping the current interval
            # merge intervals if needed
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res
