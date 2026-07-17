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

        def dfs(row, col, prevTile):
            if not (0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] > prevTile):
                return 0
            if (row,col) in visited:
                return visited[(row,col)]
            
            forwardSum = 0
            for dr, dc in directions:
                temp = dfs(row+dr, col+dc, matrix[row][col])
                if temp > forwardSum:
                    forwardSum = temp

            res = 1 + forwardSum
            visited[(row,col)] = res
            return res
        

        maxPath = 0
        for row in range(ROWS):
            for col in range(COLS):
                maxPath = max(dfs(row, col, -1), maxPath)
        return maxPath