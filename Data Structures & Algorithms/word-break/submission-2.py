class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            if not dp[i]:
                continue
            for word in wordDict:
                wordLength = len(word)
                if i + wordLength <= len(s) and s[i:i + wordLength] == word:
                    dp[i + wordLength] = True
                    
        
        return dp[-1]