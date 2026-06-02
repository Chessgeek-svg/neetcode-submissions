class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        memo = {}
        directions = [(1, 0), (0,1)]
        def dfs(row, col):
            if row >= ROWS or col >=COLS:
                return 0
            
            if row == ROWS -1 and col == COLS -1:
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            paths = 0
            for dr, dc in directions:
                paths += dfs(row + dr, col + dc)
            
            memo[(row, col)] = paths
            return paths
        return dfs(0,0)
