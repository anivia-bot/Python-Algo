'''
Given an m x n matrix board containing 'X' and 'O', 
capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
'''

'''
Solution:
The trick for solving this problem is quite brilliant.
We first need to identify that every 'O' connecting the edge 
will not be replaced/surrounded thus we peform a dfs on 
all 'O's that are starting from the edges. We replace all the 'O'
with some other char let's say 'T', then we perform another iteration to
convert all the remaining Os to X. Once the operation is done, covert the
'T's back to 'O's.

'''


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        # The time complexity would be O(N*M)
        # The space complexity would be O(N*M)
        rowLen = len(board)
        colLen = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rowLen or c >= colLen or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == 'O' and (r == 0 or r == rowLen - 1 or c == 0 or c == colLen - 1):
                    dfs(r, c)

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        return board