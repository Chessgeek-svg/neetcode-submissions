class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        def recursion(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    subset.append(nums[i])
                    used[i] = True
                    recursion(subset)
                    subset.pop()
                    used[i] = False
        recursion([])
        return res