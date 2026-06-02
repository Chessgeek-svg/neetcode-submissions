class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix = []

        for i in range(9):
            a = []
            for j in range(9):
                a.append(board[i][j])
            matrix.append(a)
        print(matrix)

        # row and column check
        for k in range(9):
            for i in range(9):
                for j in range(9):
                    if i == j:
                        continue
                    elif matrix[k][i] == matrix[k][j]:
                        if matrix[k][i] == "." or matrix[k][j] == ".":
                            continue
                        return False
                    elif matrix[i][k] == matrix[j][k]:
                        if matrix[i][k] == "." or matrix[j][k] == ".":
                            continue
                        return False

        #3x3 grid check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                numSet = set()
                for k in range(3):
                    for l in range(3):
                        if matrix[i+k][j+l] != ".":
                            if matrix[i+k][j+l] not in numSet:
                                numSet.add(matrix[i+k][j+l])
                            else:
                                return False
        return True
