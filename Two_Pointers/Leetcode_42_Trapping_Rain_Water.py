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

In sum, we have 4 ptrs, lMax, l, rMax, r. We first figure out if lMax greater or rMax greater.
if lMax is greater we can safely calculate every grid by using this 
water = max(lMax, height[l]) - height[l]

If height[l] >= lMax then we get no water as the result will always be 0
We update the index l += 1 and update lMax 

Same logic goes to r ptr.

'''

class Solution:
    def trap(self, height):
        # The time complexity would be O(N) and the space complexity would be O(1)
        if not height:
            return 0
    
        res = 0
        l = 0
        lMax = height[l]
        r = len(height) - 1
        rMax = height[r]

        while l < r:  
            # We know that right side will be greater so we can simply calculate every grids
            if lMax < rMax:
                # Calculate every grid by subtracting every height[l] it traverse till lMax is no longer < than rMax
                # Let say the grid goes as [3,4,5,6] height[l] is always increasing which means max(height[l], lMax)
                # will always be height[l] and water will be 0
                water = max(lMax, height[l]) - height[l]
                l += 1
                # update lMax to check if lMax will still be greater than rMax on the next iteration
                lMax = max(lMax, height[l])
                res += water
            else:
                water = max(rMax, height[r]) - height[r]
                r -= 1
                rMax = max(rMax, height[r])
                res += water
        return res
