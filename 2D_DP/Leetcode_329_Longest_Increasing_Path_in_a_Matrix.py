'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Solution:
This is just a simple DFS search on all index. All we need to do is to save
the max visited path value in the visited hashmap and perform dfs on all 4 directions.
All return the longest path

'''


class Solution:
    def longestIncreasingPath(self, matrix):

        # Time and space complexity would be O(N*M)
        if not matrix:
            return 0
        
        LongestPath = 1 
        visited = {}
        def dfs(i, j, prevNum):

            if (i < 0 or j < 0 or i >= len(matrix) or
                j >= len(matrix[0]) or matrix[i][j] <= prevNum):
                return 0

            if (i,j) in visited:
                return visited[(i, j)]
            
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            visited[(i, j)] = res 
            return res

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # ('-inf') is because if the path has negative values
                # we want to start make sure every node gets visited.
                # if all nodes are at least positive we can pass in 0 instead
                LongestPath = max(LongestPath, dfs(i, j, float('-inf')))
        
        return LongestPath