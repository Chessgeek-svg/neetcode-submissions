class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def dfs(subset, i):
            if i == len(nums):
                res.append(subset.copy())
                return
    
            subset.append(nums[i])        
            dfs(subset, i+1)
            subset.pop()
            dfs(subset, i+1)
        dfs(subset, 0)
        return res