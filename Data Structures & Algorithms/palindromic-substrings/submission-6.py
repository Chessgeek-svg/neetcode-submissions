class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def palindromeHelper(start, end) -> int:
            nonlocal count
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
                
        for i in range(len(s)):
            palindromeHelper(i, i)
            palindromeHelper(i, i+1)

        return count