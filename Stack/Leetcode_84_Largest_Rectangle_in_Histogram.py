'''
Given an array of integers heights representing the histogram's 
bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''

'''
Solution:
Recognizing that this is a stack problem.
if the histogram is in increasing order than we do not need to pop the stack
as we can keep extending to the right to create a new rectangle.
once we reach a smaller rectangle, we need to pop from the stack because we 
are extending to the left and see how far the current rectangle can reach.
Store how far left the smaller rectangle can reach in order for us to calculate
the max area for the samller rectangle.

The first part of the for loop is to ensure that once we dont have an increasing
rectangle. we calculate the current area of the rectangle so far and 
record how far left (we use a while loop tp go all the way left by popping the previous value from the stack)
the current (small rectangle) can reach

The second part of the for loop is to calculate all the remaining histogram.
ex: if the entire graph is in increasing order. We will only be adding more and more 
rectangle into the stack. if there are 6 rectangle the stack will have 6 values. Thus
we will be calculating the max area by height * (len(heights) - idx)

'''

class Solution:
    def largestRectangleArea(self, heights):
        # This algo runs in O(N) time and O(N) space
        maxArea = 0
        stack = []

        for idx, val in enumerate(heights):
            start = idx
            while stack and val < stack[-1][1]:
                i, height = stack.pop()
                maxArea = max(maxArea, height * (idx - i))
                start = i

            stack.append([start, val])
        
        for idx, val in stack:
            maxArea = max(maxArea, val * (len(heights) - idx))
        
        return maxArea
