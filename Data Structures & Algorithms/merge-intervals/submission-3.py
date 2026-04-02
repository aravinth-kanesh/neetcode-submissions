class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # edge case
        if not intervals:
            return []

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

        # time - sorting is O(nlogn), processing remaining intervals is
        # O(n) - merging intervals is an O(1) operation for each interval

        # space - O(n) for the final list, since it will contain all 
        # n intervals

def test_merge_intervals():
    s = Solution()

    # normal 
    assert s.merge([[1, 3], [1, 5], [6, 7]]) == [[1, 5], [6, 7]]

    # no merges
    assert s.merge([[1, 4], [6, 10]]) == [[1, 4], [6, 10]]

    # all intervals are merged
    assert s.merge([[1, 2], [2, 6], [5, 12]]) == [[1, 12]]

    # empty input
    assert s.merge([]) == []