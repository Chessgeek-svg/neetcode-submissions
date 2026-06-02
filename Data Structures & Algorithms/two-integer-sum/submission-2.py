class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indices and i != indices[difference]:
                return[i, indices[difference]]
        return -1
        