class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def bfs(square):
            visited = []
            queue = deque()
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            queue.append(square)
            edgeReached = False

            while queue:
                row, col = queue.popleft()
                if not (row in range(ROWS) and col in range(COLS)):
                    edgeReached = True
                    continue
                if board[row][col] == 'X' or (row, col) in visited:
                    continue
                visited.append((row, col))
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    queue.append((newr, newc))

            if edgeReached:
                return visited
                
            for square in visited:
                row, col = square
                board[row][col] = 'X'
            return None

        notSurrounded = set()
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row, col) not in notSurrounded:
                    vetted = bfs((row, col))
                    if vetted:
                        for square in vetted:
                            notSurrounded.add(square)

        return