'''
Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''
'''
Solution:
This problem is a relativly simple dp problem. All you need to do is to add all combination of
number sum into the dp set and if there are ever a number that is exactly half the total sum of 
the array. It means there will be a possible way to split the array into two arrays.

In sum, we first check if the total sum of the array can be divided by 2, if yes then
it is possible to split the array into two halves.
We then create a dp set to store all the possible sum out come into the sp set.
we added a 0 as a base case since there will be a time where you need to add itself into the
sp set for example, when we do a bottom up dp approach, the first number we encounter is 5
from the last index, we need to add 5 + 0 into the dp set so the set will become dp={0,5}
cloneDp.add(nums[i]+j) -> will be doing 5 + 0 and 5 + 11 etc ... 

Since we are iterating the dp, if we add element into dp it will mess up the original value
while iterating. Thus we need to set a cloneDp and update dp = cloneDp after the iteration.

'''
class Solution:
    def canPartition(self, nums):
        
        # The time complexity would be O(N*sum(nums))
        # Space complexity would be O(sum(nums))
        
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in reversed(range(len(nums))):
            cloneDp = dp.copy()
            for j in dp:
                cloneDp.add(nums[i]+j)
                if target in cloneDp:
                    return True
            dp = cloneDp
        return False

        