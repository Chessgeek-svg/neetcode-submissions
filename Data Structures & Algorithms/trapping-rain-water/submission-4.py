class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        maxLeft = height[left]
        maxRight = height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                res += max(maxLeft - height[left], 0)
                maxLeft = max(height[left], maxLeft)
            else:
                right -= 1
                res += max(maxRight - height[right], 0)
                maxRight = max(height[right], maxRight)
        return res
