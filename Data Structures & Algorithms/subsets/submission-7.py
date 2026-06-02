class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursion(nums, subset):
            nonlocal res

            if len(nums) == 0:
                res.append(subset.copy())
                return
            
            subset.append(nums[0])
            recursion(nums[1:], subset)
            subset.pop()
            recursion(nums[1:], subset)

            return

        recursion(nums, [])
        return res
