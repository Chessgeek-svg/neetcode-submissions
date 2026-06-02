class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vals = [1] * m
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                vals[j] += vals[j+1]
        return vals[0]