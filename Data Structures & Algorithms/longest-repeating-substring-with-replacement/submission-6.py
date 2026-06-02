class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        buckets = {}
        left = 0
        maxcount = 0
        res = 0
        for right in range(len(s)):
            buckets[s[right]] = buckets.get(s[right], 0) + 1
            maxcount = max(maxcount, buckets[s[right]])
            while maxcount + k <= right - left:
                buckets[s[left]] -= 1
                left += 1
            res = max(res, maxcount + k)
        return min(res, len(s))