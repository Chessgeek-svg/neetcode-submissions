class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(i, path, pathTotal):
            if pathTotal == target:
                res.append(path[:])
                return
            if pathTotal > target or i == len(nums):
                return
            
            path.append(nums[i])
            recurse(i, path, pathTotal + nums[i])
            path.pop()
            recurse(i+1, path, pathTotal)
        
        recurse(0, [], 0)
        return res