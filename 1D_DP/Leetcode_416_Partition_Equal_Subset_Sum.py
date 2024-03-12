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

'''
class Solution:
    def canPartition(self, nums):
        
        # The time complexity would be O(N*sum(nums))
        # Space complexity would be O(sum(nums))
        
        if sum(nums) % 2:
            return False
        
        dp = set()
        target = sum(nums)//2
        dp.add(0)
        
        for i in nums:
            tempSet = set()
            for j in dp:
                if (i+j) == target:
                    return True
                else:
                    tempSet.add(j+i)
                    tempSet.add(j)
            dp = tempSet
        return True if target in dp else False
        