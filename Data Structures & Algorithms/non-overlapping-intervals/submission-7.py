class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])

        res = []
        prev = float("-inf")
        for interval in intervals:
            if interval[0] >= prev:
                res.append(interval)
                prev = interval[1]
        return len(intervals) - len(res)