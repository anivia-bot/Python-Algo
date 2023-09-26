'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''
'''
Solution:
This is basically a 4 ptrs; Two ptrs approach.
The key is to have 4 ptrs l, lMax, r, rMax

We first need to distinguish which side has the lower height hence (lMax or rMax)
inorder for us the calculate how much water it can store.

Method -> if the next ptr (l+1) points to a higher value(location), 
update the lMax only quit the loop and recompare (lMax or rMax)

if the next ptr (l+1) is lower than lMax, calculate the val and update the ptr untill 
lMax get updated

repeat the same thing with rMax and r-1 ptr

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        # The time complexity would be O(N) and the space complexity would be O(1)
    
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        total = 0
        
        while l < r:  
            if lMax < rMax:
                water = max(height[l], lMax) - height[l]
                l += 1
                lMax = max(height[l], lMax)
                if water == 0:
                    continue
                else:
                    total += water
            else:
                water = max(height[r], rMax) - height[r]
                r -= 1
                rMax = max(height[r], rMax)
                if water == 0:
                    continue
                else:
                    total += water
        return total
                