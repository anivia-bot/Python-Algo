'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

'''
Solution:
This problem can either be solved by using a dict or set to track the repeated numbers.
'''
class Solution:
    def containsDuplicate(self, nums):
        # Time complexity would be O(N)
        # Space complexity would be O(N) as well
        
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False