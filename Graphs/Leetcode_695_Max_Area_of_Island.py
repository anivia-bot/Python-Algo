'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
'''

'''
Solution:
This is another number of island problem.
The only difference is to have another variable to track how many 
island it has vist and add use a max function to compare the max area
Dont forget to create a visited hash set to add all visited nodes
into the hash set.
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        res = 0
        self.count = 0
        resLen = len(grid)
        colLen = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= resLen or c >= colLen or (r, c) in visited or grid[r][c] == 0:
                return
            self.count += 1
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return

        for r in range(resLen):
            for c in range(colLen):
                if grid[r][c] == 1 and (r,c) not in visited:
                    self.count = 0
                    dfs(r, c)
                    res = max(res, self.count)
        return res