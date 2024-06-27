'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321


Solution:

There are two things to take care of in this problem, the first thing is to take care of the
negative number as python gives weird iteration when you mod a negative number. Second, Write
a two if statement to check if the 'about to add' number will exceeed the 32 bits restriction
of the software by checking if the prefix of the number will exceed or equal to the 32 bits limit.
If it will exceed, then we simply return 0, else we can safely add the number and not rasied any
exceptions or errors.
'''

class Solution:
    def reverse(self, x: int) -> int:

        # O(n) time and O(1) space (however since the longest length of the number will be 32)
        # The run time would be O(32) which is O(1)

        posBoundary = 214748364
        negBoundary = -214748364
        res = 0

        negative = False
        if x < 0:
            negative = True

        x = abs(x)
        while x: 
            lastNum = x % 10
            x = x // 10

            if res > posBoundary or (res == posBoundary and lastNum > 8):
                return 0
            if res < negBoundary or (res == negBoundary and lastNum < 7):
                return 0
            res = res*10 + lastNum

        return -1 * res if negative else res