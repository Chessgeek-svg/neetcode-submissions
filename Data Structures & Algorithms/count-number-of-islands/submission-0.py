class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        self.ROWS, self.COLS = len(grid), len(grid[0])
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] != "0" and (r, c) not in visited:
                    self.dfs(grid, r, c, visited)
                    islands += 1
                elif (r, c) not in visited:
                    visited.add((r,c))
        return islands
        #go through until finding the start of an island
        # use dfs to find the full size of the island, add every index of the island to a visited island set, increment islands by 1
    def dfs(self, grid, r, c, visited):
        if (min(r, c) < 0 or r == self.ROWS or c == self.COLS or (r, c) in visited):
            return

        visited.add((r,c))

        if grid[r][c] == "1":
            self.dfs(grid, r + 1, c, visited)
            self.dfs(grid, r - 1, c, visited)
            self.dfs(grid, r, c + 1, visited)
            self.dfs(grid, r, c - 1, visited)

      
            
        