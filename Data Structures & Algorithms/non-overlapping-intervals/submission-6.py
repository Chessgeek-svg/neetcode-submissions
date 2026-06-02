class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[1])
        prev = intervals[0][1]
        removals = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                removals += 1
            else:
                prev = intervals[i][1]
        return removals

        