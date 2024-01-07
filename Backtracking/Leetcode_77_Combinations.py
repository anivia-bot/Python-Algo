'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

'''
'''
Solution:
This is a classic backtracking problem:
Since we know that the number ranges from [1,n] use a list comp to create
a list of numbers, once the numbers have been created we can perform backtracking
to solve this problem. We first set our base case when curr == k we append to res
and when i >= len(nList) we simply return

Apply backtracking template, either include the value or not include the value.
We first append the value then we increment i+1 then we apply dfs on the next i+1 position
after we reached the end of the DFS loop, we start popping the value and began the next DFS loop
untill every combination has been created we return res.

'''



class Solution:
    def combine(self, n, k):
        nList = [n for n in range(1,n+1)]
        res = []
        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i >= len(nList):
                return
            
            curr.append(nList[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        return res