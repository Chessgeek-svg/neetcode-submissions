class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        curWater, maxWater = 0, 0

        while L <= R:
            curWater = min(height[L], height[R]) * (R - L)
            maxWater = max(curWater, maxWater)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxWater
        