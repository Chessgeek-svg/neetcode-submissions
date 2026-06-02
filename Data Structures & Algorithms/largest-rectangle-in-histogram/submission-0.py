class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stepsLeftUntilShorterHeight = [-1] * len(heights)
        stepsRighttUntilShorterHeight = [-1] * len(heights)

        for i in range(len(heights)):
            while stack and heights[i] < stack[-1][0]:
                _, stackIndex = stack.pop()
                stepsLeftUntilShorterHeight[stackIndex] = i - stackIndex
            stack.append((heights[i], i))
        while stack:
            _, stackIndex = stack.pop()
            if stepsLeftUntilShorterHeight[stackIndex] == -1:
                stepsLeftUntilShorterHeight[stackIndex] = len(stepsLeftUntilShorterHeight) - stackIndex

        stack = []
        for i in range(len(heights) -1, -1, -1):
            while stack and heights[i] < stack[-1][0]:
                _, stackIndex = stack.pop()
                stepsRighttUntilShorterHeight[stackIndex] = stackIndex - i
            stack.append((heights[i], i))
        while stack:
            _, stackIndex = stack.pop()
            if stepsRighttUntilShorterHeight[stackIndex] == -1:
                stepsRighttUntilShorterHeight[stackIndex] = stackIndex + 1


        maxArea = 0
        for i in range(len(heights)):
            area = heights[i] * (stepsRighttUntilShorterHeight[i] + stepsLeftUntilShorterHeight[i] - 1)
            maxArea = max(area, maxArea)

        return maxArea

        