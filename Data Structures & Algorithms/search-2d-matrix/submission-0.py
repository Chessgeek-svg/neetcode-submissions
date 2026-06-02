class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = [0,0]
        right = [rows-1,cols-1]
        mid = []

        while not mid or leftIndex <= rightIndex:
            leftIndex = self.indexify(left, cols)
            rightIndex = self.indexify(right, cols)
            midIndex = (leftIndex + rightIndex) // 2
            mid = [midIndex // cols, midIndex % cols]
            #print(left, mid, right)
            if target > matrix[mid[0]][mid[1]]:
                left = [mid[0], mid[1]+1]
                if left[1] >= cols:
                    left[1] = 0
                    left[0] += 1
            elif target < matrix[mid[0]][mid[1]]:
                right = [mid[0], mid[1]-1]
                if right[1] < 0:
                    right[1] = cols-1
                    right[0] -= 1
            else:
                return True
        
        return False
    
    def indexify(self, arr:List[int], cols) -> int:
        return arr[0]*cols + arr[1]

        