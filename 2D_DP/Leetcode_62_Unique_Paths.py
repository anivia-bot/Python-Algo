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
This is a relatively straight foward 2D DP problem. We first set a list of 1s as a based case
then we interate over the array in reversed order. In sum, we know that the bottom row will always
we one so we set our base case row to be all ones, We also know that the right most coloum will also
be all ones so we start our iteration from the second index. Remeber to set a tmp to be a copy since
we will be updating tmp as we iterate over the array. The formula for counting how many ways is that 
the right all possibilty from the right tmp[j+1] + all posibility from the bottom row[j].

Once we finsih calculating the row value we update row = tmp and start with the next iteration.
'''

class Solution:
    def uniquePaths(self, m, n):

        # The solution runs in O(N*M) time complexity since we will be computing every grids
        # We only defined one row as our auxiliary list so the space complexity would be O(2n) = O(N)
        
        row = [1] * n

        for i in reversed(range(m - 1)):
            tmp = row.copy()
            for j in reversed(range(n - 1)):
                tmp[j] = tmp[j+1] + row[j]
            row = tmp
        return row[0]