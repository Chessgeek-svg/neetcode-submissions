class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1, len_2 = len(word1), len(word2)
        dp = [[0 for _ in range(len_2 + 1)] for _ in range(len_1 + 1)]
        for i in range(len_1):
            dp[i][-1] = len_1 - i
        for j in range(len_2):
            dp[-1][j] = len_2 - j
        for i in range(len_1 -1, -1, -1):
            for j in range(len_2 -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        print(dp)
        return dp[0][0]