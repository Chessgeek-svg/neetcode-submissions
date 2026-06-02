class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key = lambda i : i[0])
        removals = 0
        overlap = intervals[0]
        for start, end in intervals[1:]:
            lastEnd = overlap[1]
            if start < lastEnd:
                overlap = [start, min(end, lastEnd)]
                removals += 1
            else:
                overlap = [start,end]
        return removals