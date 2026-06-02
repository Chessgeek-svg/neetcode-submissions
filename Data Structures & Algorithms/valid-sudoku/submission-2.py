class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = COLS = 9
        #Check each row for repeats
        for i in range(ROWS):
            seen = set()
            for j in range(COLS):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])
        
        #Check each col
        for j in range(COLS):
            seen = set()
            for i in range(ROWS):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])
        
        #Check each box
        for i in range(0, ROWS, 3):
            for j in range(0, COLS, 3):
                seen = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] in seen:
                            return False
                        if board[k][l] != ".":
                            seen.add(board[k][l])
        
        return True