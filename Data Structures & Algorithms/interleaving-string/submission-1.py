class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        LEN1, LEN2 = len(s1), len(s2)
        if LEN1 + LEN2 != len(s3):
            return False
        dp = [[False for _ in range(LEN2+1)] for _ in range(LEN1+1)]
        dp[-1][-1] = True

        for i in range(LEN1-1, -1, -1):
            if s1[i] == s3[i+LEN2]:
                dp[i][-1] = True
            else:
                break
        for j in range(LEN2-1, -1, -1):
            if s2[j] == s3[j+LEN1]:
                dp[-1][j] = True
            else:
                break

        for i in range(LEN1-1, -1, -1):
            for j in range(LEN2-1, -1, -1):
                if s1[i] == s3[i+j]:
                    dp[i][j] = dp[i+1][j]
                if s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j] or dp[i][j+1]
        return dp[0][0]