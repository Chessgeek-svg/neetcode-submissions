class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_frequency = res = left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_frequency = max(max_frequency, count[s[right]])
            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res