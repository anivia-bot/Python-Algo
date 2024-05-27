'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Solution:

The whole idea is to make a 2D grid and do a bottom-up DP approach.
if the chars from w1 and w2 matches then we simply fill the current index with the 
lower right dp value

    if word1[i] == word2[j]:
        dp[i][j] = dp[i+1][j+1]

vice versa we do the same thing when we cant find a match
            insert: (i, j+1)  lets say we insert a matching char into word1 
            we know that we will def match so we can move on to the next index of word2
            and see if it match with the original word1[i] char
            delete: (i+1, j) same logic, if we delete word1 we move to the next char of 
            word1 and see if it match the original w2
            replace: (i+1, j+1) we simple match the char and still cost 1 operation

    the 1+ comes from 1 operation + searching to the right, down or lower right

    else:
        1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
'''
class Solution:
    def minDistance(self, word1, word2):
        # make a 2D matrix fill with 0 and do a bottom up DP approach.
        dp = [[float('inf')]*(len(word2)+1) for _ in range(len(word1)+1)]
        # set base case for the last row and colums
        '''
            a c d _
        a [[0,0,0,3],
        b  [0,0,0,2],
        d  [0,0,0,1], 
        _  [3,2,1,0]]

        if w1[i] == w2[j]:
            -> (i+1, j+1)
        else:
            insert: (i+1, j)
            delete: (i, j+1)
            replace: (i+1, j+1)
        
        '''
        # The following for loops are to set the last row and the last coloum to be 3,2,1,0
        # for example, first index of the last row means from an empty string how many operations
        # do you need to do to create a c d -> thus that is where the 3 came from.
        for i in reversed(range(len(word2)+1)):
            dp[-1][i] = len(word2) - i
        
        for j in reversed(range(len(word1)+1)):
            dp[j][-1] = len(word1) - j

        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
                
        return dp[0][0]
        