class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        prevInterval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prevInterval[1]:
                prevInterval = [prevInterval[0], max(interval[1], prevInterval[1])]
            else:
                res.append(prevInterval)
                prevInterval = interval
        res.append(prevInterval)
        return res