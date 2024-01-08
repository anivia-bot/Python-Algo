'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
'''
'''
Solution:
The trick for this problem is to know how to map all 
diagonal index when mapping all queens.
for negative diagonal we use (r-c) 

ex: 0 1 2 3  (negative) (r-c)
  0 0 -1
  1 1 0 -1 
  2   1 0 -1
  3     1 0

ex: 0 1 2 3  (positive) (r+c)
  0     2 3
  1   2 3 4 
  2 2 3 4
  3 3 4  

From the above example we can see that all combination of the idex
will produce the same sum or difference. The key is to find the pattern.

Create a hash set for col, positive diagonal and negative niagonal.
Also create a tmp list that defaults all '.' in a 2D array.
Peform backtrack with base case when n == row since if the row went out of bounce and 
no coditions have been trigger then we can simply append the copy to res.

Use a for loop to iterate through potential Q position starting from the first idx.
Backtracking r + 1 is how the algo increase row value.
remember the remove val that has been stored in col posdig and negdig and change Q back to '.'

'''
class Solution:
    def solveNQueens(self, n):
        # Time complexity would be O(N!)
        # Space complexity would be O(N^2)

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
        return res