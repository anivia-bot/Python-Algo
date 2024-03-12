'''
You are given a 2D grid initialized with these three possible values:
-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. 
If a land cell cannot reach a treasure chest than the value should remain INF.
Assume the grid can only be traversed up, down, left, or right.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

'''
'''
Solution:
This is another classic BFS problem, rember to add all the starting point
into the q and having directions initalized.

I added current distance into the q so we can just simply += every iteration
I added on more condition newVal > grid[r][c] since it will not be the shortest path
update the grid with the shortest distance and add the current index into the q for 
further BFS iteration.
'''

from collections import deque
class Solution:
    def wallsAndGates(self, grid):
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Time and space complexity are both O(MN)
        q = deque()
        rowLen = len(grid)
        colLen = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    # pass 
                    q.append((r, c, 0))

        while q:
            # taking a snapshot of q
            # add index of val > 0 (not a wall)
            for i in range(len(q)):
                rowQ, colQ, val = q.popleft()
                # track what the new distance will be.
                newVal = val + 1
                for row, col in directions:
                    r = rowQ + row
                    c = colQ + col
                    if (r < 0 or c < 0 or r >= rowLen or c >= colLen or
                        grid[r][c] < 0 or newVal > grid[r][c]):
                        continue
                    grid[r][c] = min(newVal, grid[r][c])
                    # pass in the new distance
                    q.append((r, c, newVal))
        return grid
                

