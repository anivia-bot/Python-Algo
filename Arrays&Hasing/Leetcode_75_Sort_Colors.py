'''
Given an array nums with n objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Solution:

Basically you have 2 ptr and you swap them when you encounter 2 or 0
care for edge case where i >= bluePtr -> everything on the right of bluePtr is already sorted with 2s
same goes to red, everything on the left of redPtr is already sorted with 0s

Also as we decrement blue ptr, (same goes to all ptr/index problem) we need to check if it will still 
be inbound as it might have out of index errors.

Two for loops will swap everything in place.
'''


class Solution:
    def sortColors(self, nums):
        """
        Perform a bucket sort with one-pass solution that runs in O(N) solution and O(1) time
        Look out for edge case when swaping 0 with the right ptr
        """
        if len(nums) <= 1:
            return nums
    
        redPtr = 0
        bluePtr = len(nums) - 1

        for i in range(len(nums)):
            while bluePtr > 0 and nums[bluePtr] == 2:
                bluePtr -= 1
            if i >= bluePtr:
                break
            if bluePtr > 0 and nums[i] == 2:
                nums[bluePtr], nums[i] = nums[i], nums[bluePtr]

        for j in reversed(range(len(nums))):
            while redPtr < len(nums) and nums[redPtr] == 0:
                redPtr += 1
            if j <= redPtr:
                break
            if redPtr < len(nums) and nums[j] == 0:
                nums[redPtr], nums[j] = nums[j], nums[redPtr]
            
        return nums