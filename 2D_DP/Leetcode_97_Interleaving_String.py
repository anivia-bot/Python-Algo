'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.


Solution:

There are only two cases we have to put i < len(s1) and j < len(s2)

        d   b   b   c   a   _  (s2)
    
    a   F   F   F   F   F   F      
                    
    a   F   F   F   F   F   F
    
    b   F   F   F   F   F   F
    
    c   F   F   F   F   F   F
    
    c   F   F   F   F   F   F
    
    _   F   F   F   F   F   T
    
    (s1)
    
In this case the if we used all s1 characters and reached the 
last line i will make invalid index when we do s1[i] and vice versa for s2[j]

After conversion

        d   b   b   c   a   _  (s2)
    
    a   T   F   F   F   F   F      
                    
    a   T   F   F   F   F   F
    
    b   T   T   T   T   T   F
    
    c   F   T   T   F   T   F
    
    c   F   F   T   T   T   T
    
    _   F   F   F   F   F   T
    
    (s1)

If either the bottom or the right position is True then we can set the current position to be True
since there will be a path/solution going downwards or to the right.

When we iterate over the jth index, we check if the right to see if it is a valid path/solution
If it is not then we immediately know since the current index is False since going to the right
will not make a path. Same goes to the ith index.

For example: if we look at s1, let's say if we used all the chars from s1 and we are at the bottom
row of the matrix. We goes to the right to check to see if the previous index has a path to the end
and turns out the last char from s3 is 'c' and the last char from s2 is 'a' which we will never make 
a path thus the current index will remain to be False.

In the double for loop, we both checked for i+1 (going downward) and j+1 (going right) to see if 
there are a valid path from the previous index. If there is a valid path + the current index matches
s3 char then it makes the current index a match.
'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        # time and space are both O(N*M)
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False]*(len(s2)+1) for i in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                '''
                i and j will only go out of bound at the very last index s1[i] s2[j]
                We first check if i or j will be in bound then we check if the 
                char match, we first check s1 then we check s2.
                After that we check if i+1 (going down) can form a path.
                and we also check if j+1 (going right) can form a path.                
                '''
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True 
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]