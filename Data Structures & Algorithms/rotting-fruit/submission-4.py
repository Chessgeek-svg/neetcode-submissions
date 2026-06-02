class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruit = 0
        time = 0
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshFruit += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        if freshFruit == 0 and not queue:
            return 0
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while freshFruit > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    if (newr in range(ROWS) and 
                        newc in range(COLS) and 
                        grid[newr][newc] == 1
                    ):
                        grid[newr][newc] = 2
                        queue.append((newr, newc))
                        freshFruit -= 1
            time += 1
        return time if freshFruit == 0 else -1