class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def recursion(i, path, pathTotal):
            if pathTotal == target:
                result.append(path[:])
                return
            if pathTotal > target or i == len(nums):
                return
            
            path.append(nums[i])
            recursion(i, path, pathTotal + nums[i])
            path.pop()
            recursion(i+1, path, pathTotal)
            return

        recursion(0, [], 0)
        return result