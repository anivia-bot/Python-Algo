'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''
'''
Solution:
This is a classic DFS approach,
Just remember to take care of the condition for example:
For loop only execute when grid[r][c] == '1'
and dfs base case stops when grid[r][c] == '0'
Also create a set visited to keep track every visited nodes so
we dont do repeated work.

Use a double for loop to iterate through the rows and cols and 
use a DFS to add all visited nodes into visited.
'''


class Solution:
    def numIslands(self, grid):
        
        # The time complexity would be O(N*M)
        # The space complexity would be O(1) since we are modifying the grid in place
        if not grid:
            return 0

        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])
        island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rowLen or c >= colLen or (r, c) in visited or grid[r][c] == '0':
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    island += 1

        return island
