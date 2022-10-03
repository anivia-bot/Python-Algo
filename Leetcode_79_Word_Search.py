class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # The time complexity would be O(n*m*4^n)
        # Space complexity would be O(n*m)
        row, col = len(board), len(board[0])
        seen = set()

        def dfs(r, c, i):
            inRange = (r>=0 and c>=0 and r<row and c<col)
            if i == len(word)-1 and inRange and board[r][c]==word[-1] and (r,c) not in seen:
                return True
            if not inRange or (r,c) in seen or board[r][c] != word[i]:
                return False
            seen.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            seen.remove((r,c))
            return res 

        for x in range(row):
            for y in range(col):
                if dfs(x, y, 0):
                    return True
        return False
