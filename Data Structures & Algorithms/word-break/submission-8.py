class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        dp = [False] * (len_s + 1)
        dp[-1] = True
        for i in range(len_s -1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i + word_len <= len_s and s[i:i+word_len] == word:
                    dp[i] = dp[i+word_len]
                if dp[i]:
                    break
        return dp[0]