class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Time complexity would be O(N^2logN^2)
        # Space complexity would be O
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited.add((0,0))

        while minHeap:
            t, x, y = heapq.heappop(minHeap)
            if x == N-1 and y == N-1:
                return t
            
            for dr, dc in directions:
                newX = x + dr
                newY = y + dc
                if (newX < 0 or newY < 0 or newX >= N or
                    newY >= N or (newX, newY) in visited):
                    continue
                visited.add((newX, newY))
                heapq.heappush(minHeap, [max(t, grid[newX][newY]), newX, newY])
        return