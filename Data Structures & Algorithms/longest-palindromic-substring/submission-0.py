class Solution:
    def longestPalindrome(self, s: str) -> str:
        LEN_S = len(s)
        longestSubstring = (1, s[0]) #length, substring

        def checkLength(i1, i2):
            if i1 < 0 or i2 >= LEN_S or s[i1] != s[i2]:
                return ""
            while i1-1 >= 0 and i2+1 < LEN_S and s[i1-1] == s[i2+1]:
                i1 -= 1
                i2 += 1
            return s[i1:i2+1]

        for i in range(LEN_S):
            substring = checkLength(i, i)
            if len(substring) > longestSubstring[0]:
                longestSubstring = (len(substring), substring)

            substring = checkLength(i, i+1)
            if len(substring) > longestSubstring[0]:
                longestSubstring = (len(substring), substring)

        return longestSubstring[1]