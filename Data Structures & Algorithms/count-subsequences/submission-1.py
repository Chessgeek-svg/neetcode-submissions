class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]* (len(t)) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][0] = int(s[i] == t[0])

        for j in range(1, len(t)):
            for i in range(1, len(s)):
                if s[i] == t[j] and i >= j:
                    dp[i][j] = sum(dp[x][j-1] for x in range(i))
        return sum(dp[i][-1] for i in range(len(s)))
