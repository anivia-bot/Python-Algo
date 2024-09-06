'''
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

Solution:
This is a tricky binary search problem. The two tricks we need from our observation is that
the unique element will not match with the element on the left nor right.
Second, once we find the find the middle value, we need to decide where to update our pointers.
How? you simply just check if the left side of the mid value is odd or even. If it is even length with no
matching current value then we know everything on the left is duplicate so we update our ptr to the right.

take this as an example:

         4
[1,1,2,3,3,4,4,8,8]
if you are at index 4, even tho everything on the left is even, but you need to subtract 1 since you have a
matching 3 on the left. So you are only evaluation index 0 -> 2 which is a length of 3 (odd number)

'''

class Solution:
    def singleNonDuplicate(self, nums):
        
        l = 0
        r = len(nums) - 1 
        while l <= r:
            # Could have an edge case doing this as if l and r are both big numbers, could caused an overflow
            # ex: l and r are both 2,000,000,000 if we add then together we could cause an overflow on 32 bits
            # machine which only handles int value to 2^31 - 1 which is 2,147,483,647
            # Safer way to do it is:
            # m = l + (r - l) // 2
            m = (l+r) // 2
            leftMatch = (m-1) >= 0 and nums[m] == nums[m-1]
            rightMatch = (m+1) < len(nums) and nums[m] == nums[m+1]
            if not leftMatch and not rightMatch:
                return nums[m]

            leftSize = m - 1 if leftMatch else m

            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1