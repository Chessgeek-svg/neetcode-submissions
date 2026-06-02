class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        s_length = len(s)
        for i in range(s_length):
            count += self.helperPalindromeCounter(s, i, i, s_length)
            count += self.helperPalindromeCounter(s, i, i + 1, s_length)
        return count

    def helperPalindromeCounter(self, s, left, right, s_length):
        count = 0
        while left >= 0 and right < s_length and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count