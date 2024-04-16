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
Essentially this problem can be solve in on iteration of a loop
We need to keep track what the min and max value at an index.
For example we have an array [1,3,4,-3, 6, -7]
                    currMax   1 3 12 -3  6  1512
                    currMin   1 3 4 -36 -216 -42
At each num, we try to find out that the Max and Min value so we try it with
currMax * num, currMin * num, num   on both Max and Min 
These 3 different posibility should give the correct value of Max and Min
Update the result based on max min num and the past result

If the num is 0 its an edge case, reset everything back to 1 since
0 multiply by anything would be 0 and we can skip that number

In sum, find the max and min at each number.  

'''
class Solution:
    def maxProduct(self, nums):
        # O(N) time and O(1) space

        res = max(nums)
        currMax = 1
        currMin = 1

        for num in nums:
            if num == 0:
                currMax = 1
                currMin = 1
                continue
            
            tmp = currMax
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp * num, currMin * num, num)
            res = max(currMax, currMin, num, res)
        return res