class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        for i in range(len(s)):
            while s[i] in s[left:i]:
                left += 1
            maxLength = max(maxLength, i - left + 1)
        return maxLength