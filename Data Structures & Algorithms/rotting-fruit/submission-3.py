class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        freshFruit, minutes = 0, 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshFruit += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        while freshFruit > 0 and queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    if (newr in range(ROWS) and newc in range(COLS) and grid[newr][newc] == 1):
                        grid[newr][newc] = 2
                        queue.append((newr, newc))
                        freshFruit -= 1
            minutes += 1
        return minutes if freshFruit == 0 else -1