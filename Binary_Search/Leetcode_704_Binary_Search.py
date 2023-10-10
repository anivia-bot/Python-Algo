'''
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

'''
Solution:
This is a classic binary search problem.
use a left ptr, right ptr and mid ptr
if the value is too small right ptr = mid - 1
if the value is too big left ptr = mid + 1

while loop has to be =>  while r >= l:
if there are only one element in the list we still need to excecute the loop.

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary Seach is a O(log(n)) solution
        # Space complexity would be O(1)
        
        l = 0
        r = len(nums) - 1
        while r >= l:
            
            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1
    