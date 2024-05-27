'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Solution:
The trick for this algo is to check for all base cases and conditions.
make sure to create all base cases and conditions and runs a dfs for all possible 
outcome. 
'''

class Solution:
    def isMatch(self, s, p):

        # O(N*M) time and space complexity 
        # Caching all the index
        cache = {}
        def dfs(i, j):
            
            # Will return True if one of the base cases have been match
            # At the end of the DFS traversal one of the base case will
            # be trigger and will return True or False. The way we format the 
            # return statement with the or statement makes us return True if one 
            # of the result matches
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            
            match = i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '.')
            # for all * cases
            if j+1 < len(p) and p[j+1] == '*':
                # dfs(i, j+2) is the tricky part as we can use the char 0 times when we have '*'
                # Thats why, s[i] does NOT have to match p[j] if p[j+1] == '*' we simply ignore
                # and move to the j+2 index (since j+1 is '*')
                # If the char match and we decided to use '*' more than once then we simply increase
                # i+1 as it might match more p[j] since * can be reuse more than once.
                cache[(i, j)] = dfs(i, j+2) or (match and dfs(i+1, j))
                return cache[(i, j)]
            # for all match cases
            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            # Neither * case or match case have been matched.
            return False
        return dfs(0,0)