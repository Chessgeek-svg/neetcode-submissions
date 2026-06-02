class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def search(index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])

            if index in cache:
                return cache[index]
            result = max((nums[index] + search(index - 2), search(index - 1)))
            cache[index] = result
            return result
                
        return search(len(nums)-1)
        