class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxAmount = 0

        while left <= right:
            curHeight = min(height[left], height[right])
            curAmount = curHeight * (right - left)
            if curAmount > maxAmount:
                maxAmount = curAmount
            

            while left <= right and curHeight >= height[left]:
                left += 1
            while left <= right and  curHeight >= height[right]:
                right -= 1
            

        return maxAmount