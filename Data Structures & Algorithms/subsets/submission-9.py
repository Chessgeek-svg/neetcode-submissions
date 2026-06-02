class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recursion(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            recursion(i+1, subset)
            subset.pop()
            recursion(i+1, subset)
        
        recursion(0, [])
        return res