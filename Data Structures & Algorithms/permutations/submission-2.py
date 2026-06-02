class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        
        def backtrack(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    subset.append(nums[i])
                    visited[i] = True
                    backtrack(subset)
                    subset.pop()
                    visited[i] = False
                
        backtrack([])
        return res