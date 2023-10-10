'''
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

'''
Solution:
This is obvious a 2 pass loop solution.
First create a res array full of 1s with a len of nums
set a variable pre and post both equal to 1 and loop it to update all the prev val into the res array
loop it backwards but now times the pre val and store it in res

set res[i] *= pre
then update pre since it will be store into the next position
pre = pre*nums[i] 

repeat the same process backwards 

'''

class Solution:
    def productExceptSelf(self, nums):
        
        # The time complexity is O(N) and the space complexity would be O(N)
        res = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        
        post = 1
        for j in reversed(range(len(nums))):
            res[j] *= post
            post *= nums[j]
        return res
        