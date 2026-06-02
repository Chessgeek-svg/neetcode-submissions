class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in elements:
                continue
            curr = num
            while curr in elements:
                curr += 1
            length = curr - num
            longest = max(longest, length)
        return longest
