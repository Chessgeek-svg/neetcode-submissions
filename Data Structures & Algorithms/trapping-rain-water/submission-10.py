class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        water = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                maxL = max(maxL, height[left])
                water += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                water += maxR - height[right]
        return water