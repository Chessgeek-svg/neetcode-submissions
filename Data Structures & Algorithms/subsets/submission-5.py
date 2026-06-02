class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        len_nums = len(nums)
        def recurse(subset, start, end):
            result.append(subset.copy())

            for i in range(start, len_nums):
                subset.append(nums[i])
                recurse(subset, i+1, len_nums)
                subset.pop()
            
            return None
        recurse([], 0, len_nums)
        return result