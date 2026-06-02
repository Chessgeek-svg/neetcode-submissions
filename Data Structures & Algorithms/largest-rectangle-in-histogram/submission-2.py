class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackIndex, stackHeight = stack.pop()
                area = stackHeight * (i - stackIndex)
                maxArea = max(area, maxArea)
                start = stackIndex
            stack.append((start, h))


        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(area, maxArea)
            
        return maxArea
        