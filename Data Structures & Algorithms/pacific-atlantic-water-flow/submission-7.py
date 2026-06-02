class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        pacific = set()
        atlantic = set()

        def flow(row, col, ocean, prev):
            if not(0 <= row < ROWS and 0 <= col < COLS and (row, col) not in ocean and heights[row][col] >= prev):
                return
            
            ocean.add((row, col))
            for dr, dc in directions:
                flow(row + dr, col + dc, ocean, heights[row][col])
            
        for row in range(ROWS):
            flow(row, 0, pacific, 0)
            flow(row, COLS-1, atlantic, 0)
        
        for col in range(COLS):
            flow(0, col, pacific, 0)
            flow(ROWS-1, col,  atlantic, 0)

        return list(pacific & atlantic)