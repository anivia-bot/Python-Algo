'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
'''
'''
Solution:


'''
class Solution:
    def countSubstrings(self, s):
        # Time O(N^2) and O(1) space
        self.res = 0

        def checkP(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            checkP(i, i)
            checkP(i, i + 1)

        return self.res
