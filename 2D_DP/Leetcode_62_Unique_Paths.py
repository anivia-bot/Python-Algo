'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:

Input: m = 3, n = 7
Output: 28
'''

'''
Solution:


'''

class Solution:
    def uniquePaths(self, m, n):

        # The solution runs in O(N*M) time complexity since we will be computing every grids
        # We only defined one row as our auxiliary list so the space complexity would be O(2n) = O(N)
        
        row = [1]*n

        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]