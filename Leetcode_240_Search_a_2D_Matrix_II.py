class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Time complexity would be O(m+n) since it will try to iterate over the rows the columns
        row = len(matrix)
        col = len(matrix[0])
        colPtr = col - 1
        rowPtr = 0
        
        while colPtr >= 0 and rowPtr < row:
            if matrix[rowPtr][colPtr] == target:
                return True
            
            if matrix[rowPtr][colPtr] > target:
                colPtr -= 1
            else:
                rowPtr += 1
        
        return False