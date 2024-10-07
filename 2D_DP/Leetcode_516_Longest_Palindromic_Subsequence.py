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


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = []

        for i in range(len(text1)+1):
            tmp = []
            for j in range(len(text2)+1):
                tmp.append(0)
            dp.append(tmp)

        for i in reversed(range(len(dp)-1)):
            for j in reversed(range(len(dp[0])-1)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]