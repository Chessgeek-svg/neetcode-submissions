class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.palindromeHelper(s, i, i)
            count += self.palindromeHelper(s, i, i+1)
        return count
    def palindromeHelper(self, s, start, end):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            count += 1
        return count