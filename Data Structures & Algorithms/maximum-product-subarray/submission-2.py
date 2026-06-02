class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = subarrayMax = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i] * curMax, nums[i] * curMin)
            curMin = min(nums[i], nums[i] * curMax, nums[i] * curMin)
            curMax = temp
            subarrayMax = max(curMax, subarrayMax)
        return subarrayMax
