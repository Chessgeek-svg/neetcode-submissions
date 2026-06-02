class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                stackIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (index - stackIndex))
                start = stackIndex
            stack.append((start, height))
        
        while stack:
            stackIndex, stackHeight = stack.pop()
            maxArea = max(maxArea, stackHeight * (len(heights) - stackIndex))
        return maxArea