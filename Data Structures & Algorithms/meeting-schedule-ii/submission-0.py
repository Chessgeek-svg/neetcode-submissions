"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        q = []
        maxRooms = 0
        for interval in intervals:
            while q and q[0] <= interval.start:
                heapq.heappop(q)
            heapq.heappush(q, interval.end)
            maxRooms = max(maxRooms, len(q))
        return maxRooms