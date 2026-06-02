class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            midpoint = (start + end) // 2
            if nums[midpoint] < target:
                start = midpoint + 1
            elif nums[midpoint] > target:
                end = midpoint - 1
            else:
                return midpoint
        return -1