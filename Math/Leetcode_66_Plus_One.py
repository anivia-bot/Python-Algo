'''
You are given a large integer represented as an integer array digits, where each digits[i] is 
the ith digit of the integer. The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Solution:
Use a carry variable to track if there carry is needed in the current computation. If the digit + carry 
went over 10, simple make the current digits 0 and make the carry 1 and continue with the loop.
On edge case is when the first num has a carry. We need to append carry first then we add the remaining digits
to the res.
'''


class Solution:
    def plusOne(self, digits):

        # O(N) time and O(1) space
        
        carry = 0
        res = []
        for i in reversed(range(len(digits))):
            digit = digits[i]
            if i == len(digits)-1:
                digit += 1
            if digit + carry >= 10:
                digits[i] = 0
                carry = 1
                continue
            else:
                digits[i] = digit + carry
            carry = 0
        if carry:
            res.append(carry)
        return res + digits
