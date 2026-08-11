class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1

        def expand(l, r):
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # l and r are now one past the valid palindrome
            length = r - l - 1
            if length > max_len:
                start = l + 1
                max_len = length

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start:start + max_len]