class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            counter += self.helperPalindrome(s, i, i)
            counter += self.helperPalindrome(s, i, i+1)
        return counter

        
    def helperPalindrome(self, s: str, left: int, right: int):
        count = 0
        s_length = len(s)
        while left >= 0 and right < s_length and s[left] == s[right]:
            count += 1
            right += 1
            left -= 1
        return count