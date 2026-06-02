class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        length = len(nums)

        subset = []
        def dfs(i):
            if i >= length:
                res.append(subset.copy())
                return

            subset.append(nums[i])
        
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
            
        