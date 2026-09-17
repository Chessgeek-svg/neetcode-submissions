class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []

        min_x, max_x = 0, len(matrix) - 1
        min_y, max_y = 0, len(matrix[0]) - 1

        direction = 'right'
        while min_x <= max_x and min_y <= max_y: #when they overlap, we've iterated through all possible items
            print(spiral)
            #go right
            if direction == 'right':
                for col in range(min_y, max_y + 1):
                    spiral.append(matrix[min_x][col])
                min_x += 1
                direction = 'down'
                continue

            #go down
            if direction == 'down':
                for row in range(min_x, max_x +1):
                    spiral.append(matrix[row][max_y])
                max_y -= 1
                direction = 'left'
                continue
            
            #go left
            if direction == 'left':
                for col in range(max_y, min_y -1, -1):
                    spiral.append(matrix[max_x][col])
                max_x -= 1
                direction = 'up'

            #go up
            if direction == 'up':
                for row in range(max_x, min_x -1, -1):
                    spiral.append(matrix[row][min_y])
                min_y += 1
                direction = 'right'

        return spiral