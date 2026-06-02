class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #trying to find a rectangle with the largest area
        #area = the shorter of the two vertical walls * the number of elements between them in the array + 1
        maxWater = 0
        i, j = 0, len(heights) - 1
        while i <= j:
            length = j - i
            curWater = min(heights[i], heights[j]) * (j - i)
            maxWater = max(maxWater, curWater)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxWater