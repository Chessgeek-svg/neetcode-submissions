class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        islands = 0

        def dfs(row, col):
            if not (0 <= row < ROWS and\
                    0 <= col < COLS and\
                    grid[row][col] == "1" and\
                    (row, col) not in visited):
                return False
            
            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            return True
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col):
                    islands += 1
        
        return islands