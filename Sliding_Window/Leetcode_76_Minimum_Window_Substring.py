'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substringof s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
'''
Solution:
The trick is to realize this is a sliding window problem
if we use two dicts and compare it on every iteration we will be running in O(N*t)
since we will be checking every element in the dictionary if they have a matching count of strings

if we use a have and need to check the matching status we can reduce the run time to O(N)
variable 'need' will be the len of tDict (since there is repeating char ex: 'aaaba' need will equals to 2)
variable 'have' will be establish and change while we iterate through the string

once need and have are equal to each other (need == have) we start to shrink the left ptr untill the need == have
condition no longer satisfied
find the shortest string and store the l and r position in a list (res)
return res 

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # time complexity would be O(N)
        # space complexity would be O(1) since there are at most 26 chars in the alphabets
        
        if len(t) > len(s):
            return ''
        
        if s == t:
            return t

        sDict = {}
        tDict = {}
        res = [-1, -1]
        resLen = float("inf")
        l = 0
        r = 0

        for char in t:
            if char not in tDict:
                tDict[char] = 1
            else:
                tDict[char] += 1
        
        for char in s:
            sDict[char] = 0
        
        have = 0
        need = len(tDict)

        while r < len(s):
            rightChar = s[r]
            sDict[rightChar] += 1
            if rightChar in tDict and sDict[rightChar] == tDict[rightChar]:
                have += 1
            while have == need and l <= r:
                currentLen = (r - l + 1)
                if currentLen < resLen:
                    res = [l, r]
                    resLen = currentLen
                leftChar = s[l]
                sDict[leftChar] -= 1
                if leftChar in tDict and sDict[leftChar] < tDict[leftChar]:
                    have -= 1
                l += 1
            r += 1 
        return s[res[0]:res[1]+1] if resLen != float('inf') else ''