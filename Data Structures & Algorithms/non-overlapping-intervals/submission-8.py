class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prevInterval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] >= prevInterval[1]:
                prevInterval = interval
            else:
                count += 1
        return count