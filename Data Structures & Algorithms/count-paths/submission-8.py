class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                res[j] += res[j+1]
        return res[0]