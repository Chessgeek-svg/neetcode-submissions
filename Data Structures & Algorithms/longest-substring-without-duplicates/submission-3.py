class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, curLength = 0, 0
        left = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                curLength -= 1

            charSet.add(s[right])
            curLength += 1
            maxLength = max(maxLength, curLength)
        
        return maxLength