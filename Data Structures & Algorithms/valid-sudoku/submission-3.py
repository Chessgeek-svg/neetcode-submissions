class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = COLS = 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in rows[r] or \
                   board[r][c] in cols[c] or \
                   board[r][c] in square[(r // 3, c // 3)]:
                    return False
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r // 3, c // 3)].add(board[r][c])

        return True