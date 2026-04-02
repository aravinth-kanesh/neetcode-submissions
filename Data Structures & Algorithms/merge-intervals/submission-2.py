class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by start time - can be compared easily
        # (and linearly)
        intervals.sort(key = lambda x: x[0]) # this is an O(nlogn) operation

        # store final intervals after merged
        merged = []

        # current interval
        prev = intervals[0]

        # loop through remaining intervals
        for interval in intervals[1:]:
            # if intervals overlap, merge
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            # otherwise intervals don't match
            else:
                # append the "previous" interval to the final list,
                # since no more intervals will overlap with it
                merged.append(prev)
                prev = interval

        # final interval still needs to be added to the final list
        merged.append(prev)
        return merged 
