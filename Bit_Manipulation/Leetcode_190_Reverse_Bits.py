'''
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, 
both input and output will be given as a signed integer type. They should not affect your implementation, 
as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, 
in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents 
the unsigned integer 43261596, so return 964176192 which its binary representation is 
00111001011110000010100101000000.

Solution:
The trick for this problem is to understand bit shifting. There is one common mistake when dealing with this problem.
You need to shift the res = res << 1 first befroe adding the new bit as you need to make room for the new bit that need 
to be added. If you add the bits then shift to the left then you will go one off to the left.
For example: 

Let's say we have a bit with a len of 5 (11000) and we shift the bit then we add the number

First shift:
res = 00001
n = 01100

Second shift:
res = 00011
n = 00110

Third shift:
res = 00110
n = 00011

Fourth shift:
res = 01100
n = 00001

Fifth shift:
res = 11000
n = 00000

However if you add the bits then shift it will become

First shift:
res = 00010
n = 01100

Second shift:
res = 00110
n = 00110

Third shift:
res = 01100
n = 00011

Fourth shift:
res = 11000
n = 00001

Fifth shift:
res = 10000
n = 00000

As you can see, the result will be off by one. That is why we need to shift the bit first before
we add the newly computed bits.

'''


class Solution:
    def reverseBits(self, n):
        # O(32) -> O(1) time and O(1) space
        res = 0

        for i in range(32):
            res = res << 1
            bit = n % 2
            res += bit
            n = n>> 1
        return res