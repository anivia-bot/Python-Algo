'''
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

'''
Solution:
This problem is a classic BFS problem with a lot of set up needs to be consider.
First we need to set up time, fresh and 4 directions
Then we add up all the fresh orange count then add all the rotten oranges into the q.

Since there's an edge case where there are no fresh orange at the beginning, we add that
into the while loop condition,

Then we use a double for loop to perform iterations, on popping from the q and 
traverse through the 4 directions the of the BFS. We add all visited nodes into
visited and -= 1 on fresh and += time out side the for loop since that is one iteration 
of the BFS.

'''

from collections import deque
class Solution:
    def orangesRotting(self, grid):
        # Time complexity would be O(N*M)
        # Space complexity would be O(N*M) since we are storing all elements in the array 
        time = 0
        fresh = 0
        q = deque()
        rowLen = len(grid)
        colLen = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        # fresh > 0 is because if there's no fresh orange in the 
        # first place we dont even need to run BFS.
        while q and fresh > 0:
            for i in range(len(q)):
                rotR, rotC = q.popleft()
                for row, col in directions:
                    r = rotR + row
                    c = rotC + col
                    if (r < 0 or c < 0 or r >= rowLen or c >= colLen or 
                        (r, c) in visited or grid[r][c] == 0 or grid[r][c] == 2):
                        continue
                    visited.add((r, c))
                    q.append((r, c))
                    fresh -= 1
            time += 1
        print(fresh)
        return time if fresh == 0 else -1
