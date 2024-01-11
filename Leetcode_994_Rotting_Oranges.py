from collections import deque
class Solution:
    def orangesRotting(self, grid):
        # Time complexity would be O(N*M)
        # Space complexity would be O(N*M) since we are storing all elements in the array 
        q = deque()
        fresh = 0
        time = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        
        while q and fresh > 0:
            
            for rot in range(len(q)):
                r, c = q.popleft()
                for i, j in directions:
                    newR, newC = r+i, c+j
                    if newR >= 0 and newR < row and newC >= 0 and newC < col and grid[newR][newC] == 1:
                        q.append([newR, newC])
                        fresh -= 1
                        grid[newR][newC] = 2
            time += 1
        
        return time if fresh == 0 else -1
            