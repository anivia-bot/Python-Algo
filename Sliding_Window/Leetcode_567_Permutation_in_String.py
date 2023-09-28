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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        string1Dict = {}
        string2Dict = {}
        stringIterDict = {}

        for char in s2:
            if char not in string2Dict:
                string1Dict[char] = 0
                string2Dict[char] = 1
                stringIterDict[char] = 0
            else:
                string2Dict[char] += 1

        for char in s1:
            if char not in string2Dict:
                string1Dict[char] = 1
            else:
                string1Dict[char] += 1

        l, r = 0, len(s1)-1

        for count in range(l,r + 1):
            stringIterDict[s2[count]] += 1

        while r < len(s2):
            if string1Dict == stringIterDict:
                return True
            stringIterDict[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                stringIterDict[s2[r]] += 1

        return False
