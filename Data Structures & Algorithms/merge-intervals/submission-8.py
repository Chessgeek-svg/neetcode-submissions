class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        curr = intervals[0]
        res = []
        for i in range(len(intervals)):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                res.append(curr[:])
                curr = intervals[i]
        res.append(curr)
        return res
