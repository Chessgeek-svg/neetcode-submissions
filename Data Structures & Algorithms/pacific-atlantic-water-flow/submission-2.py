class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(row, col, visited, prevHeight):
            if ((row, col) in visited or 
            row not in range(ROWS) or 
            col not in range(COLS) or 
            heights[row][col] < prevHeight):
                return
            visited.add((row, col))

            for dr, dc in directions:
                newr, newc = row + dr, col + dc
                dfs(newr, newc, visited, heights[row][col])

        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS - 1, c, atlantic, 0)

        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS - 1, atlantic, 0)

        return list(pacific & atlantic)