class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Use Binary Search
        # Since we are searching using BST, the time complexity would be (O(log(n))
        # However we are searching on a 2D matrix, the overall time complexity would be O(log(n) * O(log(m)) = O(log(m)log(n))
        row = len(matrix)
        col = len(matrix[0])
        
        # Start from searching for the correct row using BST
        topPtr = 0
        botPtr = row - 1
        midRow = None
        
        while topPtr <= botPtr:
            midRow = (topPtr + botPtr) // 2
            if target > matrix[midRow][-1]:
                topPtr = midRow + 1
            elif target < matrix[midRow][0]:
                botPtr = midRow - 1
            else:
                break
                
        # If we are not able to find the correct row then we should return false (topPtr or botPtr has crossed each other without finding the target)
        if not topPtr <= botPtr:
            return False
        
        # Start searching the target with BST on the correct Row
        leftPtr = 0
        rightPtr = col - 1
        midCol = None
        
        while leftPtr <= rightPtr: 
            midCol = (leftPtr + rightPtr) // 2
            if target > matrix[midRow][midCol]:
                leftPtr = midCol + 1
            elif target < matrix[midRow][midCol]:
                rightPtr = midCol - 1
            else:
                return True
        return False