'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

'''
Solution:
First, check if two strings have equal length. (Anagram must have equal length)
Second, use a dictionary to track the count of each char in two strings
The first for loop tracks the count of string s
The second for loop subtrack the count in the dictionary (if any char are not in the dict or the count is 0) 
Return False else return True

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # The time complexity for this algo is O(N) + O(N) = O(N) 
        # Space complexity would be O(26) = O(1) because the most this wordCount dict would save is 26 English char.
        # It does not grow any bigger as the input increases
        checkS = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in checkS:
                checkS[i] = 1
            else:
                checkS[i] += 1
        for j in t:
            if j not in checkS:
                return False
            if checkS[j] == 0:
                return False
            checkS[j] -= 1
        return True