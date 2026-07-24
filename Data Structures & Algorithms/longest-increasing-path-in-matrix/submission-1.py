class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [
            [1,0], 
            [0,1], 
            [-1,0], 
            [0,-1]
        ]
        visited = {}

        def dfs(row, col, prev):
            if not (0 <= row < ROWS and 0 <= col < COLS and prev < matrix[row][col]):
                return 0
            if (row, col) in visited:
                return visited[(row, col)]
            
            res = 0
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                val = dfs(new_r, new_c, matrix[row][col]) 
                res = max(res, val)
            
            visited[(row, col)] = 1 + res
            return 1 + res

        longestPath = 0
        for row in range(ROWS):
            for col in range(COLS):
                longestPath = max(longestPath, dfs(row, col, -1))
        return longestPath
