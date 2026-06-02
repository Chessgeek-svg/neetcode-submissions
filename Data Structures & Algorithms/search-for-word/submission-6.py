class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i, row, col):
            if i == len(word):
                return True
            if not (0 <= row < ROWS and 0 <= col < COLS  and board[row][col] == word[i]):
                return False
            
            board[row][col] = '#'
            found = False
            for dr, dc in directions:
                if dfs(i+1, row + dr, col + dc):
                    found = True
                    break
            board[row][col] = word[i]
            return found
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
                    return True
        return False