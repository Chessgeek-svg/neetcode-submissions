class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1 
        maxL, maxR = height[left], height[right]
        total = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                maxL = max(maxL, height[left])
                total += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                total += maxR - height[right]
        return total