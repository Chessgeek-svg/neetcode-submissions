class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        step2, step1 = 0, 0
        for i in range(len(nums)):
            temp = max(nums[i] + step1, step2)
            step1 = step2
            step2 = temp

        return step2

