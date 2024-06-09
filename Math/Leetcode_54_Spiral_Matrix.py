'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Solution:

There's only one key you need to worry about for this problem. The edge case
when both top == bot and left == right. In that case we will guarentee to have 
duplicate values Thats why we set an if statement after left to right and top to down has 
been calculated once. The rest of the problem is quite straight forward. All we need is 4 
variables top down left right with 4 for loops in a while loop. After we iterate over all
of the values we simply return the res.

'''


class Solution:
    def spiralOrder(self, matrix):
        
        # Time complexity would O(N*M)
        # Space complexity would be O(N*M) if we consider the ans list as an additioanl memory
        
        res = []
        if not matrix:
            return res

        l = 0
        r = len(matrix[0])
        t = 0
        b = len(matrix)

        while l < r and t < b:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            for j in range(t, b):
                res.append(matrix[j][r-1])
            r -= 1

            # The reason we are adding this is because if we only one of the condition is met
            # we can continue the adding. If both statement is met that means we will be counting repeated work.
            if r >= l and b >= t:
                break 

            for k in reversed(range(l, r)):
                res.append(matrix[b-1][k])
            b -= 1

            for z in reversed(range(t, b)):
                res.append(matrix[z][l])
            l += 1

        return res
            

            