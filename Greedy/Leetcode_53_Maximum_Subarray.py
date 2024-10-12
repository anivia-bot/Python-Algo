'''
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Solution:
The is a simple greedy algo, all you need to do is to reset curr back to
0 whenever the total combined value is negative. This is a linear algo when we
interate over nums and use the max function to check the max total values.
'''


# Two different approach, both runs in O(N) and O(1) space

class Solution:
    def maxSubArray(self, nums):
        
        total = float('-inf')
        curr = 0

        for num in nums:
            combine = num + curr
            curr = combine
            total = max(total, combine)
            if combine < 0:
                curr = 0
        return total

# This is the two pointer solution
class Solution:
    def maxSubArray(self, nums):
        l = 0
        r = 0
        res = float('-inf')
        ptr = [0, 0]
        curr = 0

        while r < len(nums):
            curr += nums[r]
            if curr > res:
                ptr = [l, r]
                res = curr

            if curr < 0:
                r += 1
                l = r
                curr = 0
                continue
            r += 1
        return res
                
                