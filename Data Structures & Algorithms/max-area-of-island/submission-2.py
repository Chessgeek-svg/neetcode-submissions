class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                
                queue = [(i,j)]
                curArea = 0
                while queue:
                    r, c = queue.pop()
                    if not ((0 <= r < len(grid)) and (0 <= c < len(grid[0]))):
                        continue
                    if grid[r][c] == 1:
                        for dr, dc in directions:
                            queue.append((r + dr, c + dc))
                        curArea += 1
                        maxArea = max(maxArea, curArea)
                        grid[r][c] = 0

        return maxArea