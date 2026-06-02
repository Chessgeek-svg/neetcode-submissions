class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = count = maxCount = 0
        seen = set()
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                count -= 1

            seen.add(s[right])
            count += 1
            right += 1
            maxCount = max(maxCount, count)
        return maxCount