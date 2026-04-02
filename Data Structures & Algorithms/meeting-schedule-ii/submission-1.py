"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals by their start time
        intervals.sort(key = lambda x: x.start)
        # maintain a min heap of the meeting end times
        heap = []

        for interval in intervals:
            # if the meeting currently being processed starts after
            # the earliest ending meeting finishes, the room can be
            # reused
            # ensure heap is non-empty before checking if condition
            if heap and interval.start >= heap[0]:
                # remove the meeting at the top of the heap
                heapq.heappop(heap)
            # push the current meeting onto the heap
            heapq.heappush(heap, interval.end)
        
        return len(heap)
        