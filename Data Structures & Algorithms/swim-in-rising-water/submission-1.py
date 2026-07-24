class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        start = (0, 0)
        time = grid[0][0]
        frontier = [(time, start)]
        explored = set()
        while frontier:
            while frontier[0][0] <= time:
                _, (row, col) = heapq.heappop(frontier)
                if row == ROWS -1 and col == COLS -1:
                    return time
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in explored:
                        heapq.heappush(frontier, (grid[new_r][new_c], (new_r, new_c)))
                explored.add((row, col))
            time = frontier[0][0]
        print("you dun goofed")
        return -1