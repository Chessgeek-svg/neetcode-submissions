class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        for right in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[right]
            maxSum = max(maxSum, curSum)
        return maxSum