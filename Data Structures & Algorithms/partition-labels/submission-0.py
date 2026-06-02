class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        appearances = {}
        for i, char in enumerate(s):
            if char not in appearances:
                appearances[char] = [i, i]
            else:
                appearances[char][1] = i
        intervals = sorted(list(appearances.values()))
        print(intervals)
        res = [intervals[0]]
        for start, end in intervals:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        res = [res[i][1] - res[i][0] + 1 for i in range(len(res))]
        return res
