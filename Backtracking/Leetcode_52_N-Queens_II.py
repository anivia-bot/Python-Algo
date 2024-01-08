'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
'''
'''
Solution:
Essentially same as N-Queens but just return the len of the res since the result contains
Different solution of N-Queens.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDig = set() # pos (r + c)
        negDig = set() # neg (r - c)

        res = []
        tmp = [['.'] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                copy = [''.join(row) for row in tmp]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posDig or (r - c) in negDig:
                    continue
                col.add(c)
                posDig.add(r + c)
                negDig.add(r - c)
                tmp[r][c] = 'Q'

                backtracking(r + 1)

                col.remove(c)
                posDig.remove(r + c)
                negDig.remove(r - c)
                tmp[r][c] = '.'
        backtracking(0)
        return len(res)