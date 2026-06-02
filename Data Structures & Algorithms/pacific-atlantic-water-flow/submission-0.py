class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ap = {}
        res = []
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(row, col):
            if ap[(row, col)]:
                return ap[(row, col)]
            
            if row == 0 or col == 0:
                ap[(row, col)].append("pacific")
            
            if row == ROWS - 1 or col == COLS - 1:
                ap[(row, col)].append("atlantic")

            for dr, dc in directions:
                newr, newc = row + dr, col + dc
                if newr in range(ROWS) and newc in range(COLS) and heights[newr][newc] <= heights[row][col]:
                    vals = (dfs(newr, newc))
                    for val in vals:
                        if val not in ap[(row, col)]:
                            ap[(row, col)].append(val)
            return (ap[(row, col)])



        ROWS, COLS = len(heights), len(heights[0])
        for row in range(ROWS):
            for col in range(COLS):
                ap[(row, col)] = []
        for row in range(ROWS):
            for col in range(COLS):                
                dfs(row, col)
        for key, val in ap.items():
            print(key, val)
            if "pacific" in val and "atlantic" in val:
                res.append(key)

        return res
            