class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruit = 0
        numQueue = deque()
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshFruit += 1
                if grid[row][col] == 2:
                    numQueue.append((row, col))

        while freshFruit > 0 and numQueue:
            for _ in range(len(numQueue)):
                row, col = numQueue.popleft()
                for dr, dc in directions:
                    if row + dr in range(ROWS) and col + dc in range(COLS) and grid[row+dr][col+dc] == 1:
                        grid[row+dr][col+dc] = 2
                        numQueue.append((row + dr, col + dc))
                        freshFruit -= 1
            time += 1
        
        return time if freshFruit == 0 else -1
