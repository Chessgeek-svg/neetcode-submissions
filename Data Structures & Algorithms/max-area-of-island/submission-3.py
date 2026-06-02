class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandSize = 0
        def dfs(row, col, size):
            nonlocal maxIslandSize
            if not row in range(ROWS) or not col in range(COLS) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in directions:
                size += dfs(row + dr, col + dc, 1)
            maxIslandSize = max(maxIslandSize, size)
            return size
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col, 1)
        return maxIslandSize