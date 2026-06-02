class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            if grid[row][col] != "1":
                return

            grid[row][col] = "0"

            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dr, dc in directions:
                newr, newc = row + dr, col + dc
                if newr in range(ROWS) and newc in range(COLS):
                    dfs(newr, newc)

        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numIslands += 1
                    
        return numIslands
        