'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Solution:

The trick for this problem is to modify the first row and the first col to be the indication of 
which rows and cols should be set to zeros. Since at position 0,0 col and row will intersect, we
use another variable called rowZero to make keep track if rowZero needs to be filled with zeros.

In sum, we set a rowZero variable so that we dont have duplicate calculation, we iterate over the 
entire 2D matrix then we set the first row and col to 0 in the corresponding position. If row == 0
and we found a 0 in the 0th row, we set rowZero to be True.
Next we iterate over the entire 2D matrix besides the first row and col and fill them with 0s
Next if the 0,0 position is 0 then that means col = 0 will all be 0s
Next we check if rowZero == True, if True we set all value at row == 0 to be 0s.

We first iterate over the matrix to find which rows and cols need to be filled with 0s, we then 
iterate the over the matrix except first row and col and fill then matrix with zeros. Next we check 
if col 0 and row 0 needs to be filled with zero by check the first element matrix[0][0] and rowZero.


'''


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # O(N*M) time and O(1) space

        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0
        if rowZero:
            for j in range(cols):
                matrix[0][j] = 0