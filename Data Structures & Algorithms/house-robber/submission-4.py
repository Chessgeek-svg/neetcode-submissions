class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def search(index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            return max((nums[index] + search(index - 2), search(index - 1)))
                
        return search(len(nums)-1)
        