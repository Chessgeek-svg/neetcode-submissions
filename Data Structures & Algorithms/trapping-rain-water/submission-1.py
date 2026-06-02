class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        volume = 0
        prev_height = 0
        distance = r - l - 1
        while distance > 0:
            min_height = min(height[r], height[l])
            if min_height > prev_height:
                volume += distance * (min_height - prev_height)
                prev_height = min_height
            if height[l] < height[r]:
                l += 1
                volume -= min(height[l], prev_height)
            else:
                r -= 1
                volume -= min(height[r], prev_height)
            distance = r - l - 1
            print(volume, prev_height, min_height, l, r)

        return volume