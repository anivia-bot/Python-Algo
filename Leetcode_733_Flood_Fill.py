class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # The time complexity would be O(N*M) or O(N) as in every elements in the matrix
        # Space complexity would be O(h) as we are performing a DFS recursively. h means the height of memories 
        # occupied on the callstack
        
        row = len(image)
        col = len(image[0])
        centerColor = image[sr][sc]
        
        def dfs(i, j):
            
            if i < 0 or i >= row or j < 0 or j >= col:
                return

            if image[i][j] == color or image[i][j] != centerColor:
                return
            
            image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i,j+1)
            dfs(i,j-1)

        dfs(sr, sc)
        return image