class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        max_l, max_r = heights[l], heights[r]
        area = 0
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                max_l = max(heights[l], max_l)
                area += (max_l - heights[l])
            else:
                r -= 1
                max_r = max(heights[r], max_r)
                area += (max_r - heights[r])

        return area