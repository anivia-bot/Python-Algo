'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
'''
'''
Solution:
This is a non trivial tortoise and hare cycle detection problem
First we need to realize that the begining of a cycle will have multiple
ptr pointing at it and we know that it is the duplicate number

Second we need to find where the fast and slow ptr intersect. 
Because the point of the intersection between slow and fast ptr to the beginning
of the cycle is the same as the point from the beginning to the starting of the cycle

2 slow = fast 
2 (p + c - x) = p + 2c - x  
=> p - x = 0 => p = x

p => starting pt to cycle starting pt
c => len of the entire cycle
x => slow and fast ptr intersect pt to cycle starting pt
'''

class Solution:
    def findDuplicate(self, nums):       
        # O(N) time and O(1) space 
        
        slow = 0
        fast = 0
        # Use the Floyd's Tortoise and Hare algorithm to detect a cycle.
        while True:
            # Move the slow pointer one step.
            slow = nums[slow]
            # Move the fast pointer two steps.
            fast = nums[nums[fast]]
            
            # If the slow and fast pointers meet, a cycle exists.
            if slow == fast:
                break
        
        # To find the duplicate number, reset one pointer to the start.
        slow2 = 0
        while True:
            # Move both pointers at the same speed.
            slow = nums[slow]
            slow2 = nums[slow2]
            
            # When they meet again, the meeting point is the duplicate number.
            if slow == slow2:
                return slow