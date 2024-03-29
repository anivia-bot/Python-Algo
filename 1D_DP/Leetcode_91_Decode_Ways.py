'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters 
using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
'''
'''
Solution:

'''
class Solution:
    def numDecodings(self, s):

        # O(N) time and O(1) space
        if s[0] == "0":
            return 0
    
        twoBack = 1
        oneBack = 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = oneBack
            doubleDigits = int(s[i-1:i+1])
            if doubleDigits >= 10 and doubleDigits <= 26:
                current += twoBack
            twoBack = oneBack
            oneBack = current
        return oneBack
print("hi")