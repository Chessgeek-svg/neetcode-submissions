class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, row, col):
            if i == len(word):
                return True
            if 0 > row or row == ROWS or 0 > col or col == COLS or word[i] != board[row][col]:
                return False
                

            board[row][col] = '#'
            res = False
            for dr, dc in directions:
                if dfs(i+1, row + dr, col + dc):
                    res = True
            board[row][col] = word[i]
            return res

        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
                    return True
        return False
        


