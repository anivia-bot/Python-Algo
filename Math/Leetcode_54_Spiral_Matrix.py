class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Time complexity would O(N*M)
        # Space complexity would be O(N*M) if we consider the ans list as an additioanl memory
        
        ans = []
        rowS, colS = 0, 0
        rowE, colE = len(matrix)-1, len(matrix[0])-1
        
        while rowE >= rowS and colE >= colS:

            for i in range(colS, colE+1):
                ans.append(matrix[rowS][i])

            for j in range(rowS+1, rowE+1):
                ans.append(matrix[j][colE])

            for x in reversed(range(colS, colE)):
                if rowS == rowE:
                    break
                ans.append(matrix[rowE][x])

            for y in reversed(range(rowS+1, rowE)):
                if colS == colE:
                    break
                ans.append(matrix[y][colS])
            
            rowS += 1
            colS += 1
            rowE -= 1
            colE -= 1
        return ans
            
            