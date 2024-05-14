'''
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''
'''
Solution:

This is a 2D dynamic programming problem. First we set a 2D matrix fill with 0s.
Then we iterate over the matrix using a bottom up DP approach. We start from the lower
right corner. Whenever we found a match of letter we set the current index to be
1 + whatever value it is at the i+1 and j+1 index (this means the next char from both
strings since i+1 will be text1 next string and j+1 will be text2 next string). 
The other case is when we doing find a match, We store the max common subsequence
we found so far and store it in the current index, it can comes from either your 
current index to the right or to the bottom.


    a  c  e  
a   3  2  1  0

b   2  2  1  0

c   2  2  1  0

d   1  1  1  0

e   1  1  1  0

    0  0  0  0

In sum, the outer 0s is your base case, whenever you found a match is where you 
starts increasing the value (1+dp[i+1][j+1]), why is it i+1 and j+1 ? Because we
need to find the next char for both string and see what is the possible outcome 
from the next string. Take c in this example, c in the middle matches, we then
took 1 + dp(e and d) since they are the next index and we know that even though
e and d does not match, but the remaining string (de and e) have at least one more match.
That's why wee need to update the current index with whatever 
from the left dp[i][j] = max(dp[i+1][j], dp[i][j+1]) or whatever from the bottom.

'''

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # Time and Space are both O(N*M)

        dp = []
        for i in range(len(text1)+ 1):
            tmp = []
            for j in range(len(text2) + 1):
                tmp.append(0)
            dp.append(tmp)

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]