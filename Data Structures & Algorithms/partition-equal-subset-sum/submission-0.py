class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums) / 2

        def recursiveSum(index, subset):
            curSum = 0
            for i in range(len(nums)):
                if i in subset:
                    curSum += nums[i]
            if curSum == half:
                return True
            if curSum > half or index >= len(nums):
                return False
            
            subset.append(index)
            if recursiveSum(index+1, subset):
                return True
            subset.pop()
            if recursiveSum(index+1, subset):
                return True
            return False
        
        return recursiveSum(0, [])
