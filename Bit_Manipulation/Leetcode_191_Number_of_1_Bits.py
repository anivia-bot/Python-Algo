'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).
Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.


Solution:
If we iterate the int and divided by 2 every time then we can get how many 0s it has.
Thats why we use res += n % 2 

For example we have a num 13 all we do is
13 % 2 => 1, then divided by 2, 6 % 2 => 0, then divided by 2, 3 % 2 => 1, 
then divided by 2, 1 % 2 = 1, then divided by 2
Thus we get 1101 as an result. We can also shift the bit by 1 for n instead of
divided by 2.
'''


class Solution:
    def hammingWeight(self, n):

        # O(32) time -> O(1) time and O(1) space
        res = 0
        while n != 0:
            res += n % 2
            # n = n // 2 also works as well 
            n = n >> 1
        return res