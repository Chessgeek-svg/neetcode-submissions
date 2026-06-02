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
                elif grid[row][col] == 2:
                    queue.append((row, col))
        if freshFruit == 0 and not queue:
            return 0

        while queue:
            if freshFruit == 0:
                return minutes
            for i in range(len(queue)):
                r, c = queue.popleft()
                for y, x in directions:
                    newr, newc = r+y, c+x
                    if min(newr, newc) < 0 or newr == ROWS or newc == COLS or grid[newr][newc] != 1:
                        continue
                    
                    queue.append((newr, newc))
                    grid[newr][newc] = 2
                    freshFruit -= 1
            minutes += 1
        
        return -1

        