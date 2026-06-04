class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        guy = len(nums)
        for i in range(len(nums)):
            guy ^= i
            guy ^= nums[i]
        return guy