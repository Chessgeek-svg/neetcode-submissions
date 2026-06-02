class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, subset, i, picked):
            if i == len(nums):
                res.append(subset[:])
                return
            
            for j in range(len(nums)):
                if not picked[j]:
                    subset.append(nums[j])
                    picked[j] = True
                    dfs(nums, subset, i + 1, picked)
                    subset.pop()
                    picked[j] = False
            
        dfs(nums, [], 0, [False] * len(nums))
        return res
