'''
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
 
'''

'''
Solution:
This is a middle out algo is to basically iterate over the entire string and use a middle out 
approach to check if t string is a palindrom, The only thing we need to make sure is that
we need to check for both odd and even len of the string with both l, r starting from i and 
l starting from i and r starting from i + 1

'''

class Solution:
    def longestPalindrome(self, s):
        
        # Middle out algo will take O(N^2) time complexity
        # The first N time complexity would be iterate through the entire string, the N time 
        # complexity would be checking if the current string is a palindrom
        # O(1) space complexity
        
        self.res = ''
        self.resLen = 0
        
        def checkPalindrom(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currentStringL = r - l + 1
                if currentStringL > self.resLen:
                    self.res = s[l:r+1]
                    self.resLen = currentStringL
                l -= 1
                r += 1
        
        for i in range(len(s)):
            
            # odd string cases
            l, r = i, i
            checkPalindrom(l, r)
                        
            # even string cases
            l, r = i, i + 1
            checkPalindrom(l, r)
            
        return self.res
            