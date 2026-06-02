class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = float("-inf")

        for n in nums:
            curSum = max(curSum, 0) + n
            maxSum = max(maxSum, curSum)
        return maxSum
        