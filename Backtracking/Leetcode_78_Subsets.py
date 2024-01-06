'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''
'''
Solution:
This is a backtracking problem,
All we need to be careful is how we make the dicision tree
The two decision will be add value or removing value
hence, subset.append() and subset.pop(), we increment the i value by 1
and set a base case when i >= to the len of nums (at this point we need to
save the copy of the subset and return)
'''
class Solution:
    def subsets(self, nums):
        
        # The time complexity would be O(n*(2^n)) as we are using a backtracking approach
        # The decision would be either include nums[i] or don't include it. That is where the 2 is coming from.
        # Space complexity would be O((2^n)) as we store all the subsets

        res = []        
        subset = []

        def dfs(i):
            
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res