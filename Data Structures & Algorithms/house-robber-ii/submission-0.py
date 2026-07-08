class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robSelected(nums):
            rob1prev, rob2prev = 0, 0
            for num in nums:
                rob2prev, rob1prev = rob1prev, max(rob1prev, rob2prev + num)
            return rob1prev

        return max(robSelected(nums[1:]), robSelected(nums[:-1]))
            
