'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an 
unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

'''
Solution:
The trick for this problem is to split the array into left and right side
left side means that the mid val is the greatest on the left side
right side mean that the mid val is the smallest on the right side

after identifying the ptr position. write if statement to decide if 
the ptr are in the rage of left or ride side. move the ptr accordingly

Dont worry too much about have the value of left ptr > right ptr
Just focus on spliting the array into either left portion or right portion (since one of them will definately matches)
Once you split them into left portion of the array and right portion of the array check if target is in the range of
l -> m  or r -> m  

'''

class Solution:
    def search(self, nums, target):
        
        l = 0
        r = len(nums)

        while r >= l:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # left portion of the list
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right portion of the list
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                

