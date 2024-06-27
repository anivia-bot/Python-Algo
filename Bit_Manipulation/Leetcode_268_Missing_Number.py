'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Solution:
There are two solutions that can achieve O(n) time and O(1) solutions.
The first one is relatively straight forward, you sum up nums and nums+1 then subtract the two.
The difference will be the missing number.

The other way to approach this problem is by using XOR in bot manioulation, you first set a res 
to be 0 then perform XOR on every element in nums. Once you are done you perform res on the
nums + 1 array and all the duplicate number will be perfectly cancel out with the XOR operation, 
except that one unique value.
'''


class Solution:
    def missingNumber(self, nums):

        # O(N) time O(1) space
        cnt = 0
        for i in range(len(nums)+1):
            cnt += i
        return cnt - sum(nums)
    
class Solution:
    def missingNumber(self, nums):
        res = 0
        for num in nums:
            res = res ^ num

        for i in range(len(nums)+1):
            res = res ^ i
        
        return res
