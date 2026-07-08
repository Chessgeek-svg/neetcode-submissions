class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1prev, rob2prev = 0, 0
        for num in nums:
            temp = max(rob2prev + num, rob1prev)
            rob2prev = rob1prev
            rob1prev = temp
        return rob1prev
