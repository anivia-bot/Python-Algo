'''
Given a string s, partition s such that every 
substring of the partition is a palindrome
Return all possible palindrome partitioning of s.
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
'''
'''
Solution:
The tricky part is to realize why we are passing in j+1 to the DFS call
let's say we have a string 'aaab' we first check the first letter 'a'
if its a palindrome, we then try to process all combination of the remaining 
string hence, 'aab' and so on (j+1) --> 'ab' (j+1) --> ('b') once all options have been
exhausted, we then pop the tmp list to see if there are other option when j increase in the 
for loop. EX: ['a','a', 'ab' ] is ab a pali ? NO, if its not a pali we push it back further.
Ex: ['a', 'aa'] is 'aa' a pali ? Yes, when then add it to tmp and start pushing further by adding 'b'
--> ['a', 'aa', 'b'] 

        def dfs(i):
            if i >= len(s):
                res.append(tmp.copy())
                return
            for j in range(i, len(s)):
                if self.checkPalindrome(s, i, j):
                    tmp.append(s[i:j+1])
                    dfs(j + 1)
                    tmp.pop()

This format isn't too obvious like other backtracking problem, be aware! 
Same as other backtracking problem, you either include the value or you don't include the value 
with the condition that the value should be a Palindrome.
The way we use a for loop and our dfs idx to cleverly create our combination is something
that you need to keep in mind with lot's of practice. Good luck !

'''

class Solution:

    def checkPalindrome(self, s, l, r):
        # Time complexity would be O(N*2^N)
        # Space complexity would be (N^2) one N from the call stack and the other N is from the tmp list
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s):
        res = []
        tmp = []
        
        def dfs(i):
            if i >= len(s):
                res.append(tmp.copy())
                return
            for j in range(i, len(s)):
                if self.checkPalindrome(s, i, j):
                    tmp.append(s[i:j+1])
                    dfs(j + 1)
                    tmp.pop()
        dfs(0)
        return res