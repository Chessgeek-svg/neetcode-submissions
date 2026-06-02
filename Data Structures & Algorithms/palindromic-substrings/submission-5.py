class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.palindromeHelper(s, i, i)
            count += self.palindromeHelper(s, i, i+1)
        return count

    def palindromeHelper(self, s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count