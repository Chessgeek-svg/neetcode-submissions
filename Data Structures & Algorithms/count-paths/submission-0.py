class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        prevRow = [0] * COLS

        for i in range(ROWS-1, -1, -1):
            curRow = [0] * COLS
            curRow[-1] = 1
            for j in range(COLS-2, -1, -1):
                curRow[j] = curRow[j+1] + prevRow[j]
            prevRow = curRow
        return curRow[0]


