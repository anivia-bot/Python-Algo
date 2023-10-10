'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
'''
Solution:
This is another classic sliding window problem
The trick is to realize that this is a sliding window problem

Use a hash set to track all the char that has appeared.
Once a repeated char has appeared, use a while loop to 
remove all the char until we find the repeated char so 
we can start expending again.
return the max longest sub string

'''

class Solution:
    def lengthOfLongestSubstring(self, s):

        if not s:
            return 0

        charSet = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
        