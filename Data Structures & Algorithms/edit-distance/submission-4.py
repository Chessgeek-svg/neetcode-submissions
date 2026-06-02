class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)
        dp = [[0 for col in range(COLS+1)] for row in range(ROWS+1)]

        for i in range(ROWS):
            dp[i][-1] = ROWS - i
        for j in range(COLS):
            dp[-1][j] = COLS - j

        for i in range(ROWS -1, -1, -1):
            for j in range(COLS -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        print(dp)
        
        return dp[0][0]