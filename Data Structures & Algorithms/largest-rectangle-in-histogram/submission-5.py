class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                area = stackHeight * (index - stackIndex)
                maxArea = max(maxArea, area)
                start = stackIndex
            stack.append((start, height))
        
        while stack:
            stackIndex, stackHeight = stack.pop()
            area = (len(heights) - stackIndex) * stackHeight
            maxArea = max(maxArea, area)
        
        return maxArea