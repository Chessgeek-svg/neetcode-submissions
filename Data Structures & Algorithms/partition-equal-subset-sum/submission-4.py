class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target /= 2
        dp = {0}
        for n in nums:
            dp = {s + n for s in dp} | dp
            if target in dp:
                return True
        return False