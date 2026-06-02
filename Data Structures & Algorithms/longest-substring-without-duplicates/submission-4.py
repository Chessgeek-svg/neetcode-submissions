class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        L = 0
        maxLength = 0

        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[L])
                L += 1
            
            charset.add(s[R])

            maxLength = max(maxLength, R - L + 1)
        
        return maxLength
