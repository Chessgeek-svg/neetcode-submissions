class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        res = []
        used_array = [False] * len_nums
        def recursion(subset):
            if len(subset) == len_nums:
                res.append(subset[:])
                return
            
            for i in range(len_nums):
                if not used_array[i]:
                    used_array[i] = True
                    subset.append(nums[i])
                    recursion(subset)
                    subset.pop()
                    used_array[i] = False
            
            return
        
        recursion([])
        return res