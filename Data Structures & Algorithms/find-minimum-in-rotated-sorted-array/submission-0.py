class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midpoint = (end + start) // 2
            if start == end:
                break
            if nums[midpoint] < nums[end]:
                end = midpoint
            else:
                start = midpoint + 1
        return nums[midpoint]