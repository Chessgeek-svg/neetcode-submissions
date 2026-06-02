class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, maxLength = 0, 0
        curLength = 0
        charSet = set()
        for R in range(0, len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                curLength -= 1
                L += 1
            charSet.add(s[R])
            curLength += 1
            maxLength = max(curLength, maxLength)
        return maxLength