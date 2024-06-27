'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Solution:

Simply iterate over the entire nums and do an XOR operation on the num and all the 
duplicate nums will be cancel out eventually except for that one unique value.
'''


class Solution:
    def singleNumber(self, nums):

        # O(N) time and O(1) space
        res = 0

        for num in nums:
            res = res ^ num
        return res