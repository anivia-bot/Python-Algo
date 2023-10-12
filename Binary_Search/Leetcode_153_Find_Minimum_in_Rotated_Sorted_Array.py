'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, 
return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
'''
'''
Solution:
There are many edge cases for this problem (Be aware !)
This problem is just like any other binary search problem except 
we need to distinguish if we are at the left sorted portion or the
right sorted portion

if we ever encounter a time where the val at the r ptr is > than the val 
ar the l ptr then we perform a check of min val

find the middle index and check for min val
right an if statement to check if m is greater than l
if True then we are in the left side of the array so we move our
ptr to mid + 1. The same can be apply to the right ptr.
Ex:  [3,4,5,1,2]
            l r
the right ptr still needs to perform mid - 1 operation.

'''


class Solution:
    def findMin(self, nums):

        # Time complexity runs in O(logN) and O(1) space
        
        minNum = nums[0]
        l, r = 0, len(nums) - 1

        while r >= l:
            if nums[r] >= nums[l]:
                minNum = min(nums[l], minNum)
            
            m = (l + r) // 2
            minNum = min(nums[m], minNum)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minNum