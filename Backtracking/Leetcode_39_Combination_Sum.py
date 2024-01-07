'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that 
sum up to target is less than 150 combinations for the given input.
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
'''
'''
Solution:
The difference between combination and subset is that 
subset does not have duplicate values hence the decision tree will be
either include the value or not include BUT! i index will always be i + 1
However, in this combination example we can either include the value or not 
same as how we encounter in subsets. BUT! the difference will be i can remain the same
and if we dont want to include the value we perform i + 1

Since we are moving i index forward, we can make sure that there are no permutation 
For example: [2,2,3] and [2,3,2] 

'''

class Solution:
    def combinationSum(self, candidates, target):
        # Time complexity would be O(2^t) as t is the target size or the height of the decision tree
        # Since we are making 2 decisions every time so we are having a 2 to the power solution
        # The space complexity would be O(H) as H would be the height of the tree 
        
        res = []
        sub = []

        def dfs(i, total):
            if total == target:
                res.append(sub.copy())
                return
            if total > target or i >= len(candidates):
                return
            candidate = candidates[i]
            sub.append(candidate)
            dfs(i, total + candidate)
            sub.pop()
            dfs(i + 1, total)
        dfs(0,0)
        return res 

