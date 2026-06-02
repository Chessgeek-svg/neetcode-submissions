class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for left in range(len(nums)):
            middle = left + 1
            end = len(nums) - 1
            while middle < end:
                if nums[left] + nums[middle] + nums[end] == 0:
                    res.append((nums[left], nums[middle], nums[end]))
                    middle += 1
                    end -= 1
                elif nums[left] + nums[middle] + nums[end] < 0:
                    middle += 1
                elif nums[left] + nums[middle] + nums[end] > 0:
                    end -= 1
        return list(set(res))