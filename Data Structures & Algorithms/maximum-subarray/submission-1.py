class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = float("-inf")
        for n in nums:
            curSum = max(0, curSum) + n
            maxSum = max(curSum, maxSum)
        return maxSum
        