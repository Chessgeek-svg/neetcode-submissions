class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 1:
                    continue
                if r == ROWS-1 and c == COLS-1:
                    return length
                
                visited.add((r,c))
                
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for x, y in directions:
                    queue.append((r+x,c+y))
                
            length += 1
        return -1

        


            
