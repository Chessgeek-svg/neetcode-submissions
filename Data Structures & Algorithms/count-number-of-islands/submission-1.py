class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or (i, j) in visited:
                    continue
                print(visited)
                queue.append((i, j))
                while queue:
                    r,c = queue.popleft()
                    if not ((0 <= r <= len(grid) - 1) and (0 <= c <= len(grid[0]) - 1)):
                        continue
                    if grid[r][c] == "1" and (r,c) not in visited:
                        for a,b in directions:
                            queue.append((r+a, c+b))
                    visited.add((r,c))
                islands += 1
        return islands
