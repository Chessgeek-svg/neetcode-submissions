class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        truthArray = [False] * (len(s) +1)
        truthArray[-1] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i + word_len <= len(s) and s[i:i+word_len] == word:
                    truthArray[i] = truthArray[i+word_len]
                if truthArray[i]:
                    break
        return truthArray[0]