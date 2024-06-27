'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Solution:

Kinda think of it as a dp problem where you need to look back on the work you already computed.
Since this is a bit operation, the number goes up with the value of multiplication of 2 
For Example:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

When we reached a power of 2 it added a number 1, look at number 2 and 4.
Just imagine if we divided by 2 the remainder will be the remaining bits
-> lets say for the number 5 -> 101 the left most 1 is the newly formed number 
from 4, so you can read it as '1' + '01' which is '4' + '1

'''



class Solution:
    def countBits(self, n):
        # O(N) time and O(N) space
        dp = [0] * (n + 1)
        powerTrack = 1

        for i in range(1, n + 1):
            if powerTrack * 2 == i:
                powerTrack = i
            dp[i] = 1 + dp[i - powerTrack]
        return dp