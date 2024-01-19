'''
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
The rain starts to fall. At time t, the depth of the water everywhere is t. 
You can swim from a square to another 4-directionally adjacent square if and only if the elevation of 
both squares individually are at most t. You can swim infinite distances in zero time. Of course, 
you must stay within the boundaries of the grid during your swim.
Return the least time until you can reach the bottom right square (n - 1, n - 1) 
if you start at the top left square (0, 0).

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
'''
'''
Solution:
Instead of using a q, we use minHeap since this is Dji algo.
We start by add the height and idex to the heap and add the starting 
value 0,0 to visited since we will be popping off in the beginning.
We pop from the heap and set our base case to be N-1 for r and c since
if we pop a value that is at the target index then we return
Else, we utilze the directions list we have and add all the possible neighbor to the
heap, rembr to pass in the max values as we are keep track of the highest height of the path
the min heap will simply pick the shortest path for us.
'''
from collections import heapq
class Solution:
    def swimInWater(self, grid):
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