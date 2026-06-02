class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_volume = 0
        len_heights = len(heights)
        for i in range(len_heights):
            start = i
            while stack and heights[i] < stack[-1][1]:
                stack_index, stack_height = stack.pop()
                volume = stack_height * (i - stack_index)
                max_volume = max(max_volume, volume)
                start = stack_index
            stack.append((start, heights[i]))
        while stack:
            stack_index, stack_height = stack.pop()
            volume = stack_height * (len_heights - stack_index)
            max_volume = max(max_volume, volume)
        return max_volume