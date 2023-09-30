'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''
'''
Solution:
This is another sliding window problem, however the matching strings are not inorder (permutation)
In another words, since the orders are not sequensial. It will be best to use a dictionary to
track the count of each char has appeared so far.

First initalize both s1 and sInt dict to be filled with all zeros for every s2 char
Second += 1 on all s1 char that appeared in the s1 dict
initalize the first len(s1) substring in s2
use the window size of s1 and start shifting to the right 
untill we have a matching dicts for s1 dict and sInt dict 
subtrack the count of left ptr when shifting to the right
l += 1 and r += 1 and check if r + 1 is out of bounce

'''

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        if s1 == s2:
            return True

        s1Dict = {}
        sIntDict = {}

        for s in s2:
            if s not in s1Dict:
                s1Dict[s] = 0
                sIntDict[s] = 0
        
        for s in s1:
            if s not in s1Dict:
                return False
            s1Dict[s] += 1
        
        for i in range(len(s1)):
            sIntDict[s2[i]] += 1
        
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if sIntDict == s1Dict:
                return True
            sIntDict[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                sIntDict[s2[r]] += 1
        return False

