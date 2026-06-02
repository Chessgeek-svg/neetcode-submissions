class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                visited.add((r, c))
                return 0

            visited.add((r, c))
            area = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for [y, x] in directions:
                area += dfs(r+y,c+x)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited:
                    continue
                maxArea = max(maxArea, dfs(r, c))
                
        return maxArea


