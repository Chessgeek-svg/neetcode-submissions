class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        res = 0
        maxfreq = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfreq = max(maxfreq, count[s[right]])
            if maxfreq + k < right - left + 1:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res