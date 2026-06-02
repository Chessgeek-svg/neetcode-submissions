class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        truthArray = [False] * (len(s) + 1)
        truthArray[len(s)] = True
        for i in range(len(s), -1, -1):
            if not truthArray[i]:
                continue
            for word in wordDict:
                word_length = len(word)
                if i - word_length >= 0 and s[i - word_length:i] == word:
                    truthArray[i - word_length] = True
        return truthArray[0]
