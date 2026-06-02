class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row, col, visited, prevHeight):
            if (row not in range(ROWS) or 
            col not in range(COLS) or 
            (row, col) in visited or 
            heights[row][col] < prevHeight):
                return
            
            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for row in range(ROWS):
            dfs(row, 0, pacific, 0)
            dfs(row, COLS - 1, atlantic, 0)

        for col in range(COLS):
            dfs(0, col, pacific, 0)
            dfs(ROWS - 1, col, atlantic, 0)

        return list(pacific & atlantic)
