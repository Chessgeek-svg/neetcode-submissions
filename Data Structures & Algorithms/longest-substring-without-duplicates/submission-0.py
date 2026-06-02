class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, maxLength = 0, 0
        curLength = 0
        stringSet = set()
        for R in range(0, len(s)):
            if s[R] not in stringSet:
                stringSet.add(s[R])
                curLength += 1
                maxLength = max(curLength, maxLength)
            else:
                while s[L] != s[R]:
                    stringSet.remove(s[L])
                    curLength -= 1
                    L += 1
                L += 1
        return maxLength