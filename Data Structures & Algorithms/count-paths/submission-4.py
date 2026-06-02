class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        paths = [0] * COLS
        paths[-1] = 1
        for row in range(ROWS -1, -1, -1):
            for col in range(COLS -2, -1, -1):
                paths[col] += paths[col+1]
        return paths[0]
