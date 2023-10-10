'''
You are given a string s and an integer k. You can choose any character of the string and 
change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
'''

'''
Solution: 
The trick for this problem is to realize this is a sliding window problem
The key is also to understand that the most freq letter (so far) + k will be the max
length a string (sliding window) can be. if the condition 'k + maxF < (r - l + 1)' is not 
satisfied it means that it is no longer a valid string. Thus we reduce the left ptr to the right
and reduce the count in the dictionary untill a valid string can satisfied 
this 'k + maxF < (r - l + 1)' condition. Compare the lenght of the string so far and update the res.


'''
class Solution:
    def characterReplacement(self, s, k):
        count = {}
        l = 0
        maxF = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            maxF = max(maxF, count[s[r]])
            while k + maxF < (r - l + 1):
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
                
        return res


