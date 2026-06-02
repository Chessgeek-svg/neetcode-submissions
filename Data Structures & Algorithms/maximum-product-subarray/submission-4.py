class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = subarrayMax = nums[0]
        for num in nums[1:]:
            temp = max(num, curMax * num, curMin * num)
            curMin = min(num, curMin * num, curMax * num)
            curMax = temp
            subarrayMax = max(subarrayMax, curMax)
        return subarrayMax