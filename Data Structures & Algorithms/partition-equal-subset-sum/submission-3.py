class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target /= 2
        used = [0] * len(nums)
        def recurse(i, total):
            if total == target:
                return True
            if total > target or i == len(nums):
                return False
            
            used[i] = 1
            if recurse(i+1, total + nums[i]):
                return True
            used[i] = 0
            if recurse(i+1, total):
                return True
            return False
        return recurse(0, 0)