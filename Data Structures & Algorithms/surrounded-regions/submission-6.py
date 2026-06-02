class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]


        def search(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 'O'):
                return
            board[row][col] = '#'
            for dr, dc in directions:
                search(row + dr, col + dc)
        
        for row in range(ROWS):
            search(row, 0)
            search(row, COLS - 1)
        
        for col in range(COLS):
            search(0, col)
            search(ROWS -1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'