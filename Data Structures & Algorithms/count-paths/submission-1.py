class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        paths = [0] * COLS
        paths[-1] = 1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-2, -1, -1):
                paths[c] += paths[c+1]
        
        return paths[0]
