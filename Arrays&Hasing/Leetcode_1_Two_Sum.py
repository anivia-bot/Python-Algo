'''
Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

'''
Solution:
Use a dictionary to track what the next target value
iterate through the nums list, store the diff in dict
once the current num equals to the current diff then we return its index.
'''
class Solution:
    def twoSum(self, nums, target):

        # Time complexity for this solution will be O(N) Space complexity will be O(N) 
        
        seen = {}
        for idx, val in enumerate(nums):
            nextVal = target - val
            if val in seen:
                return [idx, seen[val]]
            seen[nextVal] = idx