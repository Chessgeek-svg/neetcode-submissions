class Solution:
    def rob(self, nums: List[int]) -> int:
        rob2, rob1 = 0, 0
        for i in range(len(nums)):
            temp = max (rob1, rob2 + nums[i])
            rob2 = rob1
            rob1 = temp
        return rob1