class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (m+1)
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[j] += dp[j+1]
        return dp[0]