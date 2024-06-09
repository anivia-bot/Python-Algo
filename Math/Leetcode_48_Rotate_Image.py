'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


Solution:

The trick for this problem is that, you can keep a temp variable and insert the values in reversed
order. The bottom left goes to the top left and so on until we reached top right and we simply
insert the previous saved stop left variable.
top and bottom can be l and r since we are dealing with a square.

r-l since we want i to always starts from 0 -> (r-l)
'''


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1

        while r > l:
            # Since i will always be incrementing from 0 -> whatever value
            # if we do range(l, r-1) -> l might start from 2, 3, 4
            # we donting want our l + i be l + 2 or l + 3 on the first iteration of an inner loop
            for i in range(r-l):
                top = l
                bottom = r

                topLeft = matrix[top][l+i]
                # Bottom Left to Top Left
                matrix[top][l+i] = matrix[bottom-i][l]
                # Bottom Right to Bottom Left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # Top Right to Bottom Right
                matrix[bottom][r-i] = matrix[top+i][r]
                # Top Left to Top Right
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1
