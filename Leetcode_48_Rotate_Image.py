class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #O(N*M) time and O(1) space

        l = 0
        r = len(matrix) - 1

        while r > l:

            for i in range(r - l):
                top = l
                bot = r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bot - i][l]
                matrix[bot - i][l] = matrix[bot][r - i]
                matrix[bot][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft 
            r -= 1
            l += 1