class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        self.paths = 0
        
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 1:
                return
            if r == ROWS-1 and c == COLS-1:
                self.paths += 1
                return

            visited.add((r, c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for [y, x] in directions:
                dfs(r+y,c+x)
            
            visited.remove((r, c))
            return

        dfs(0,0)
                
        return self.paths


