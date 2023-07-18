class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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