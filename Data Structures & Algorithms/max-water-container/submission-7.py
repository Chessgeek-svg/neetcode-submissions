class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        max_water = 0
        while l < r:
            dist = r - l
            max_water = max(max_water, dist * min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_water