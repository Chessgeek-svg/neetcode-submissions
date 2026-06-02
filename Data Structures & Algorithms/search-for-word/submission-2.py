class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, row, col, visited):
            if i == len(word):
                return True
            if (row, col) in visited or 0 > row or row == ROWS or 0 > col or col == COLS:
                return False

            if (row, col) not in charMap:
                charMap[(row, col)] = board[row][col]
                
            if word[i] == charMap[(row, col)]:
                visited.append((row, col))
                for dr, dc in directions:
                    if dfs(i+1, row + dr, col + dc, visited):
                        return True
                visited.pop()
            return False

        charMap = {}
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col, []):
                    return True
        return False
        


