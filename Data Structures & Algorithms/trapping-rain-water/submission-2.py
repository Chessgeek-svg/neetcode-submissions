class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        res = 0
        minHeight = 0

        while L < R:
            curHeight = min(height[L], height[R])
            if curHeight > minHeight:
                res += (curHeight - minHeight) * (R-L)
                minHeight = curHeight
            if height[L] < height[R]:
                L += 1
                res -= min(minHeight, height[L])
                res = max(res, 0)
            else:
                R -= 1
                res -= min(minHeight, height[R])
                res = max(res, 0)

        return res

