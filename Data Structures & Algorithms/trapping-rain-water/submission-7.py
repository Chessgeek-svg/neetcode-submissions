class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        res = 0
        while left < right:
            if height[left] > height[right]:
                right -= 1
                maxRight = max(height[right], maxRight)
                res += maxRight - height[right]
            else:
                left += 1
                maxLeft = max(height[left], maxLeft)
                res += maxLeft - height[left]
        return res
        