class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][0]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(prev[:])
                prev = intervals[i]
        res.append(prev)
        return res