class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # The solution runs in O(N*M) time complexity since we will be computing every grids
        # We only defined one row as our auxiliary list so the space complexity would be O(2n) = O(N)
        
        row = [1]*n

        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]