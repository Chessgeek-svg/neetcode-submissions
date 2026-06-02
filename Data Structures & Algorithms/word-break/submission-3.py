class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        truthArray = [False] * (len(s) + 1)
        truthArray[len(s)] = True
        for i in range(len(s), -1, -1):
            if truthArray[i] == False:
                continue
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    truthArray[i - len(word)] = True
        return truthArray[0]
