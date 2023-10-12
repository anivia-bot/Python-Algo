'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

'''
Solution:
Since the matrix is sorted. We can use binary search to find the correct row
then use another binary search to find the correct col.

Use if statement to compare if the first Val in that row is greater or smaller 
than the target val. if it is smaller than we move our ptr to the top 
if it is greater than we check if the target is less than the last element in the list
if yes then we found the correct row. If not we move our top ptr down

Perform another binary search again. Since this is just a 1D array.
Just use a left and right ptr to run.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        
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