'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''

'''
Solution:
This is almost identical to subsets II except have a target value to match
Since we are ignoring duplicates, we sort the input values to make our life 
easier downstream. 

Set up some base bases such as when we found the target val etc etc
Peform the backtracking templete.
Since the array is already sorted, include the while loop after curr.pop() to avoid duplicate


            curr.append(c)
            backtracking(i+1, curr)
            curr.pop() 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i+1, curr)

'''



# Time complexity would be O(2^N) and space will be O(N)
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backtracking(i, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if sum(curr) > target or i >= len(candidates):
                return
            c = candidates[i]
            curr.append(c)
            backtracking(i+1, curr)
            curr.pop() 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i+1, curr)
        backtracking(0, [])
        return res
