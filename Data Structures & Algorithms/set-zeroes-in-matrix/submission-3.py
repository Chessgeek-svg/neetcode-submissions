class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        topRow, leftCol = matrix[0][0],matrix[0][0]
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row == 0:
                        topRow = 0
                    if col == 0:
                        leftCol = 0
                    matrix[0][col] = 0 #max(matrix[0][col], -1)
                    matrix[row][0] = 0 #max(matrix[row][0], -1)

        for col in range(1, COLS):
            if matrix[0][col] == 0:
                for row in range(ROWS):
                    matrix[row][col] = 0
        for row in range(1, ROWS):
            if matrix[row][0] == 0:
                for col in range(COLS):
                    matrix[row][col] = 0
        if topRow == 0:
            for col in range(COLS):
                matrix[0][col] = 0
        if leftCol == 0:
            for row in range(ROWS):
                matrix[row][0] = 0