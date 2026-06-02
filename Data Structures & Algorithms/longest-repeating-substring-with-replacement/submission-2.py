class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        buckets = [0] * 26
        left = 0
        maxcount = 0
        for right in range(len(s)):
            bucket_index = ord(s[right]) - ord('A')
            buckets[bucket_index] += 1
            count = max(buckets)
            while count + k <= right - left:
                bucket_index = ord(s[left]) - ord('A')
                buckets[bucket_index] -= 1
                count = max(buckets)
                left += 1
            maxcount = max(maxcount, count + k)
        return min(maxcount, len(s))