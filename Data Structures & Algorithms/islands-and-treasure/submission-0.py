class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                   q.append((grid[row][col], row, col)) #pathSum, row, col
        while q:
            pathSum, row, col = q.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] > pathSum + 1:
                    grid[new_row][new_col] = pathSum + 1
                    q.append((pathSum + 1, new_row, new_col))
