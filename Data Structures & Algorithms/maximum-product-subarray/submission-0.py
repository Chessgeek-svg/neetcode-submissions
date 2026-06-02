class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        posArray = [[] for _ in range(len(nums))]
        negArray = posArray[:]
        posArray[0] = nums[0]
        negArray[0] = nums[0]
        for i in range(1, len(nums)):
            posArray[i] = max(nums[i], (posArray[i-1] * nums[i]), (negArray[i-1] * nums[i]))
            negArray[i] = min(nums[i], posArray[i-1] * nums[i], negArray[i-1] * nums[i])
        return max(posArray)