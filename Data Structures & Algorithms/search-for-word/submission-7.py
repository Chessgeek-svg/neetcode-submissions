class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, len_word = len(board), len(board[0]), len(word)
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i, row, col):
            if i == len_word:
                return True
            
            #If not the next letter in the word, return False
            if not (0 <= row < ROWS and 0 <= col < COLS and board[row][col] == word[i]):
                return False
            
            #Mutate the cell so that it can't be reused
            board[row][col] = '#'

            returnVal = False
            for dr, dc in directions:
                if dfs(i+1, row + dr, col + dc):
                    returnVal = True
                    break
            
            #Restore cell to correct val for future checks
            board[row][col] = word[i]
            return returnVal
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
                    return True
        return False