'''
Given an integer array nums, find a 
subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''
'''
Solution:

'''
class Solution:
    def maxProduct(self, nums):
        # O(N) time and O(1) space

        res = max(nums)
        currentMax = 1
        currentMin = 1

        for num in nums:
            tmpMax = num * currentMax
            currentMax = max(num * currentMax, num * currentMin, num)
            currentMin = min(tmpMax, num * currentMin, num)
            res = max(currentMax, res)

        return res