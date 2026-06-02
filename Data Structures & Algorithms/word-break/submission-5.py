class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        truthArray = [False for char in range(len_s + 1)]
        truthArray[len_s] = True
        for i in range(len_s -1, -1, -1):
            for word in wordDict:
                len_word = len(word)
                if i + len_word <= len_s and s[i:i+len_word] == word:
                    truthArray[i] = truthArray[i+len_word]
                if truthArray[i]:
                    break
        return truthArray[0]