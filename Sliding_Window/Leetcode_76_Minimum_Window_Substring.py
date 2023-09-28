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

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # time complexity would be O(N)
        # space complexity would be O(1) since there are at most 26 chars in the alphabets
        
        if t == "":
            return ""
        
        countT = {}
        window = {}
        have = 0
        res = [-1,-1]
        resLen = float('inf')
        l = 0
        
        for c in t:
            if c not in countT:
                countT[c] = 1
            else:
                countT[c] += 1
                
        need = len(countT)
        
        for r in range(len(s)):
            i = s[r]
            if i not in window:
                window[i] = 1
            else:
                window[i] += 1
                
            if i in countT and countT[i] == window[i]:
                have += 1
            

            while have == need:
                sLen = (r - l + 1)
                if sLen < resLen:
                    resLen = sLen
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]