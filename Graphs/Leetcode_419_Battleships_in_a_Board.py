'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', 
return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, 
they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), 
where k can be of any size. At least one horizontal or vertical cell separates between two battleships 
(i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Solution:

This is a simple DFS on all the battleship that exist, since battleship won't be able to connect with
each other and the battleship won't be adjcent. We guarentee that when we perform a DFS the path will
mark the battleship and we simply increase the count and save it to seen.
'''
# Time will be O(n*M) and space will be O(N*M) as well, if you are allowed to modified the input matrix
# You can reduce the space complexity to O(N) or O(M) to which ever is the largest battleship as we
# travese through the DFS will increase the call stack.

class Solution:
    def countBattleships(self, board):
        
        seen = set()
        rows = len(board)
        cols = len(board[0])
        cnt = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == '.':
                return
            if (r, c) in seen:
                return
            seen.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in seen or board[i][j] == '.':
                    continue
                dfs(i , j)
                cnt += 1
        return cnt 
