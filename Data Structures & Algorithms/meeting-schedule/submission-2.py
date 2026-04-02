"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        if n == 1:
            return True

        # sort by start times
        intervals.sort(key = lambda x: x.start)

        for i in range(n - 1):
            # overlapping
            if intervals[i].end > intervals[i + 1].start:
                return False

        return True
