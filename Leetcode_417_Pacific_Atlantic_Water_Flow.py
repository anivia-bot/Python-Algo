class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time complexity would be O(N*M)
        # Space complexity would be O(N*M)
        rowLen = len(heights)
        colLen = len(heights[0])
        pacSet = set()
        altSet = set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r >= rowLen or c >= colLen or
                 (r,c) in visited or heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(colLen):
            dfs(0, c, pacSet, heights[0][c])
            dfs(rowLen - 1, c, altSet, heights[rowLen - 1][c])
        
        for r in range(rowLen):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, colLen - 1, altSet, heights[r][colLen - 1])
        
        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) in pacSet and (r, c) in altSet:
                    res.append([r,c])
        return res

