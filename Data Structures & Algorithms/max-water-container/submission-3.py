class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0
        while l <= r:
            min_height = min(heights[l], heights[r])
            distance = r - l
            volume = distance * min_height
            if volume > max_volume:
                max_volume = volume
            if min_height == heights[l]:
                l += 1
            if min_height == heights[r]:
                r -= 1
        return max_volume