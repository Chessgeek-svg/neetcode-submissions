class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        fresh, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        while queue and fresh != 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    if newr in range(ROWS) and newc in range(COLS) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        fresh -= 1
                        queue.append((newr, newc))
            time += 1
        return time if fresh == 0 else -1