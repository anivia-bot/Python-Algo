class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Space and Time complexity are both O(M*N)
        if not grid:
            return
        islandArea = 0
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])
        self.count = 0

        def dfs(r, c):
            if not (r < 0 or c < 0 or r >= rowLen or c >= colLen or (r, c) in visited or grid[r][c] == 0):
                visited.add((r, c))
                self.count += 1 
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            return 0


        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1 and (r, c) not in visited:
                    self.count = 0
                    dfs(r, c)
                    islandArea = max(islandArea, self.count)
        return islandArea