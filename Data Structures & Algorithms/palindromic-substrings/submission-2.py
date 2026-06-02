class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0
        for i in range(len(s)):
            palindrome_count += self.palindromeCounter(s, i, i)
            palindrome_count += self.palindromeCounter(s, i, i+1)
        return palindrome_count

    def palindromeCounter(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count