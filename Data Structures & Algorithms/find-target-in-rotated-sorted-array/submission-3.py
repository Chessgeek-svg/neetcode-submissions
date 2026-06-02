class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1 
        while left <= right:
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return midpoint
            
            if nums[left] <= nums[midpoint]:
                if target > nums[midpoint] or target < nums[left]:
                    left = midpoint + 1
                else:
                    right = midpoint - 1
            else:
                if target < nums[midpoint] or target > nums[right]:
                    right = midpoint -1
                else:
                    left = midpoint + 1
        return -1