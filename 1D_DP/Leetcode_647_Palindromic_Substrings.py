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
This is another classic middle out approach, iterate over the string and check if it is a palindrom.
Be care of odd and even string len as we need to change the input of l = i and r = i + 1

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
            # odd
            checkP(i, i)
            # even
            checkP(i, i + 1)

        return self.res
