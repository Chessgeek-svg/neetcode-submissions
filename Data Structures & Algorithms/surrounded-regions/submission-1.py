class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def capture(row, col):
            if not row in range(ROWS) or not col in range(COLS):
                return
            if grid[row][col] == 'O':
                grid[row][col] = 'C'
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    capture(newr, newc)


        for row in range(ROWS):
            if grid[row][0] == 'O':
                capture(row, 0)
            if grid[row][COLS - 1] == 'O':
                capture(row, COLS - 1)

        for col in range(COLS):
            if grid[0][col] == 'O':
                capture(0, col)
            if grid[ROWS - 1][col] == 'O':
                capture(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 'C':
                    grid[row][col] = 'O'
                elif grid[row][col] == 'O':
                    grid[row][col] = 'X'