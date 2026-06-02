class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1, len_2 = len(word1), len(word2)
        dp = [[0 for j in range(len_2 +1)] for i in range(len_1 +1)]

        for i in range(len_1, -1, -1):
            for j in range(len_2, -1, -1):
                dp[i][j] = abs((i-j) - (len_1 - len_2))
        for i in range(len_1 -1, -1, -1):
            for j in range(len_2 -1, -1, -1):
                if i == j:
                    print(i, j, word1[i] == word2[j])
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        print(dp)
        return dp[0][0]