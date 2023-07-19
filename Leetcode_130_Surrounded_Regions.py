class Solution:
    def solve(self, board: List[List[str]]) -> None:
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