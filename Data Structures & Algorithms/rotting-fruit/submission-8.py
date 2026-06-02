class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        freshFruit = time = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    freshFruit += 1

        while freshFruit > 0 and queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if 0 <= new_r < ROWS and\
                       0 <= new_c < COLS and\
                       grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        freshFruit -= 1
            time += 1
        return time if freshFruit == 0 else -1