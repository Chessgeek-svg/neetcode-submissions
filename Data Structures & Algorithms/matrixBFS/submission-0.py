class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS -1 and c == COLS -1:
                        return length
                        
                neighbors = ([0,1], [1,0], [0,-1], [-1,0])
                for dr, dc in neighbors:
                    newr, newc = r+dr, c+dc
                    if min(newr, newc) < 0 or newr == ROWS or newc == COLS or grid[newr][newc] == 1 or (newr,newc) in visited:
                        continue
                    queue.append((newr,newc))
                    visited.add((newr,newc))
            length += 1
        return -1

        