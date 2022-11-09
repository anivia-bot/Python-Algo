class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

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
