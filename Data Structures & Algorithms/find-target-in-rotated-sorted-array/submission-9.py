class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midpoint = (start + end) //2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] < nums[end]:
                if nums[midpoint] < target <= nums[end]:
                    start = midpoint + 1
                else:
                    end = midpoint - 1
            else:
                if nums[start] <= target < nums[midpoint]:
                    end = midpoint -1 
                else:
                    start = midpoint + 1
        return -1