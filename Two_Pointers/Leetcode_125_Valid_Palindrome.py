'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

'''
Solution:
This is a classic two pointers problem so we need a left and right pointers
since we are ignoring spaces, common and upper case letters we will need 
an if condition to prevent while running our while loop

if s[l] or s[r] is not alphanumeric we simply update the ptr and skip the
current iteration by using 'continue'

if both s[l] and s[r] are alpha, we convert it into lower case letters then
we compare if both strings are equal to each other.
if not return False, if true update ptr right and left
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Try to do a two pointers solution would be O(N)
        # Space complexity would be O(1)
        
        l = 0
        r =  len(s) - 1
    
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
                