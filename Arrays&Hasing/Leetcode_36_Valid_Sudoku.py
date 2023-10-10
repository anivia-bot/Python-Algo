'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

'''
Solution:
This problem is pretty straightfoward, 
All you need to do is set up 3 dicts for col, rows and position (little cube for the sudoku board)
Use a double for loop to store all appeared numbers. If there are repeated nums appeared return False

The trick is store the pos key into the dict. Using  (i//3, j//3) to store all pos into this key
if there are nums appeared again return False

'''
import collections

class Solution:
    def isValidSudoku(self, board):

        # Time complexity and space complexity would be O(9^2) so technically it is O(1)
        # But if we increase the size of the board then it will be O(N^2) 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        pos = collections.defaultdict(set)

        rowsL = len(board)
        colsL = len(board[0])

        for i in range(rowsL):
            for j in range(colsL):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in pos[(i//3, j//3)]):
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                pos[(i//3, j//3)].add(board[i][j])
        return True
