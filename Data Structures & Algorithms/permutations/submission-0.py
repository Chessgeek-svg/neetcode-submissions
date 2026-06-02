class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, subset, i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in set(subset):
                    subset.append(nums[j])
                    dfs(nums, subset, i + 1)
                    subset.pop()
            
        dfs(nums, [], 0)
        return res
