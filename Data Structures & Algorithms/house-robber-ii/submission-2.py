class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def robHelper(nums) -> int:
            rob1Prev, rob2Prev = 0, 0
            for i in range(len(nums)):
                rob1Prev, rob2Prev = max(rob1Prev, rob2Prev + nums[i]), rob1Prev
            return rob1Prev

        skipFirstHouse = robHelper(nums[1:])
        skipLastHouse = robHelper(nums[:-1])
        return max(skipFirstHouse, skipLastHouse)