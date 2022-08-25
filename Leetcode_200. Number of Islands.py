class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # The time complexity would be O(N*M)
        # The space complexity would be O(1) since we are modifying the grid in place
        if not grid:
            return 0
        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >=len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = '0'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
        
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                elif grid[i][j] == '1':
                    dfs(grid, i, j)
                    island += 1
        return island