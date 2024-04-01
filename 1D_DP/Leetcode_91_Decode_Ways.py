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

Think of this problem as another climbing stair problem, however, 
instead of keep increasing the accumlated steps we ONLY increase when
there are two digits that have formed. Let's say everything is initalize to 0
in an array but in this case we only have 2 variables to track (thats why we set curr to be 0) 
ex [0,0,0,0,0,1] -> curr = 0 at every iteration

if we face a 0 then the curr 0 will be insert in the spot where 0 is. So when we look back one spot
we know it is impossible to have to form any char when the value is 0. In another words
Let's say we have a value 111006 -> the result will be 0. the first 0 will be insert into oneBack, 
we then interate forward the second 0 will be insert into twoBack. Thus we will not have any possiblity
to decode. 

In sum we set curr = oneBack since one digit will not increase the variation of strings
if i->i+2 (i+2 will not be included so it will only be i and i + 1) is a valid 2 digits
then incrase curr to be += twoBack. Why ? because at the curr index i,
"Both twoBack and oneBack can reach to the currIdx" ex: 3 posibility at twoBack, 2 possiblity at oneBack
In total there are 5 ways to reach the current index
, so curr = oneBack then curr += twoBack

Update oneBack and twoBack after we calculated the updated curr.
'''
class Solution:
    def numDecodings(self, s):

        # O(N) time and O(1) space
        if not s or s[0] == '0':
            return 0
        
        oneBack = 1 if int(s[-1]) != 0 else 0
        twoBack = 1

        for i in reversed(range(len(s)-1)):
            curr = 0
            if s[i] == '0':
                twoBack = oneBack
                oneBack = curr
                continue
            curr = oneBack

            doubleDig = int(s[i:i+2])
            if 10 <= doubleDig <= 26:
                curr += twoBack
            twoBack = oneBack
            oneBack = curr
        return oneBack