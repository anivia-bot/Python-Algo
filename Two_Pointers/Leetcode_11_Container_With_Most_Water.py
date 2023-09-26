'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

'''
Solution:
This is another classic two pointers problem
The trick is to update the smaller ptr so we maximize the water area.

'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # This algo runs in O(N) time as it traverse through the entire array
        # The space compelexity would be O(1) since we didnt use any auxiliary data structure
        
        p1 = 0
        p2 = len(height)-1
        maxWater = 0
        
        while p2 > p1:
            
            if height[p1] >= height[p2]:
                maxWater = max(maxWater, height[p2]*(p2-p1))
                p2 -= 1
            
            elif height[p2] >= height[p1]:
                maxWater = max(maxWater, height[p1]*(p2-p1))
                p1 += 1
            
        return maxWater