class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # Time and Space complexity would be O(m*n) and space would be O(n)
        cache = {}

        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i,j)]
            
        return dfs(0,0)            

