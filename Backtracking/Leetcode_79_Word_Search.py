'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''
'''
Solution:
This question is a relatively simple dfs approach.
First define the row and col len, then define a seen hashset
Second write a dfs function with some base cases.
if tmp == Word: return True,             
if (r < 0 or c < 0 or r >= rowLen or c >= colLen or 
                word[idx] != board[r][c] or (r,c) in seen):
                return False

add the current coordinates r, c into seen.
perform dfs on 4 directions, add the current word into tmp words and update the index
remove the coordinates from seen and return (top or down or left or right) if any of the
path returns true then it means we found a match at one point.

iterate through with r and c (since this decide where the starting point is)
'''
class Solution:
    def exist(self, board, word):
        
        # The time complexity would be O(n*m*4^n)
        # Space complexity would be O(n*m)
        rowLen = len(board)
        colLen = len(board[0])
        seen = set()
        
        def dfs(r, c, idx, tmpWord):
            if tmpWord == word:
                return True
            if (r < 0 or c < 0 or r >= rowLen or c >= colLen or 
                word[idx] != board[r][c] or (r,c) in seen):
                return False
            
            seen.add((r, c))
            left = dfs(r-1, c, idx+1, tmpWord + board[r][c])
            right = dfs(r+1, c, idx+1, tmpWord + board[r][c])
            down = dfs(r, c-1, idx+1, tmpWord + board[r][c])
            top = dfs(r, c+1, idx+1, tmpWord + board[r][c])
            seen.remove((r, c))
            return (top or down or left or right)

        for r in range(rowLen):
            for c in range(colLen):
                if dfs(r, c, 0, ''):
                    return True
        return False