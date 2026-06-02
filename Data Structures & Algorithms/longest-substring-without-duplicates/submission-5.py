class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        L, maxLength = 0, 0

        for R in range(len(s)):
            if s[R] in mp:
                L = max(mp[s[R]] + 1, L)
            
            mp[s[R]] = R

            maxLength = max(maxLength, R-L+1)
        return maxLength