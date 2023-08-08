class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

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
                LongestPath = max(LongestPath, dfs(i, j, float('-inf')))
        
        return LongestPath