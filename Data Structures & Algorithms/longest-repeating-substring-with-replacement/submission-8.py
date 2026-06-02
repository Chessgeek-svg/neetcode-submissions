class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        maxfreq = 0
        res = 0
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            maxfreq = max(maxfreq, counts[s[i]])
            while (i - left + 1) - maxfreq > k:
                counts[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res