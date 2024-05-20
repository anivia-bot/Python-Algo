'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Solution:
This is a relativly easy hard problem. All you need to do is to distinguish that 
we can use a cache and iterate using dfs on all the possible combinations with a 
decision tree. You can choose to use the current index i or not use the current index i.
Be careful with the base case and put j >= len(t) as we might reach the end of both strings
at the same time. The remain algo has been well commented in the coding portion.
'''

class Solution:
    def numDistinct(self, s, t):
        cache = {}
        def dfs(i, j):
            '''
            The reason we put j >= len(t) before i is because let's say we
            have two exact strings s= 'apple' and 'apple'. When we perform our
            dfs, we reached the end at the same time i=4, if we put i>=len(s)
            before j>=len(t) 0 will be return instead of 1 even after we found
            a perfect match.
            '''
            # If we reached the end of string t which means we found a path
            if j >= len(t):
                return 1
            # If we reached the end of string s and we have NOt found a path
            if i >= len(s):
                return 0
            # If we already computed (i, j) in the past and we can simply just return the result
            if (i, j) in cache:
                return cache[(i, j)]
            '''         
            There are two decisions if we found a string that matches, 
            we can choose to use up the current s string and
            the current t string and move both pointer to the next index. i+1 and j+1
            We can also not use the current string from s and try to find a matching string
            later. (i+1, j) i+1 means keep on searching in s j remains at the same index 
            since it has not been burned.

            Essentially, the two decision is choose to use s string and not to use it
            '''
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
            # Since we did not find a pair we can simply move to the next index of s
            # and try to dins it the remaining of string s
                cache[(i, j)] = dfs(i+1, j)
            # We return cache[(i,j)] after we first computed the index of (i, j) back to the previous dfs.
            return cache[(i, j)]
        return dfs(0,0)
