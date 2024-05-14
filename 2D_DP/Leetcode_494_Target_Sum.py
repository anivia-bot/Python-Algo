'''

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' 
before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate 
them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


Solution:
In sum we are using cache and dfs to store all visited index/values.
We add all possible values and we pass it upwards to (0,0)
No need to worry about values are being repeated since we can do +1+1-1 or -1+1+1 or +1-1+1 which both results in 
i=3 and total=2 --> (i,total) -> (3,2) -> which we already computed in the past and these are unique paths.

Run the dfs and return the value from (0,0)
'''
class Solution:
    def findTargetSumWays(self, nums, target):
        # O(N*T) time and space
        cache = {}
        def dfs(i, total):
            # At the end of the DFS if the result == target then we do a +1 
            # else we dont add anything
            if i == len(nums):
                return 1 if total == target else 0
            # The reason we can just return the cache is because we are doing a decision tree
            # and we are always traversing in different paths.
            # For example we can do +1+1-1 or -1+1+1 or +1-1+1 which both results in 
            # i=3 and total=2 --> (i,total) -> (3,2) -> which we already computed in the past
            # and no need to be computed again.
            if (i, total) in cache:
                return cache[(i, total)]
            
            # how many possible ways if we add the current values
            adding = dfs(i + 1, total + nums[i])
            # how many possible ways if we subtract the current values
            subtracting = dfs(i + 1, total - nums[i])
            # cache[(i, total)] -> The key is to track index and numbers total sum 
            # and the value is how many possible ways to create
            
            # lets say when we add the possible ways from adding and subtracting
            # we will know how many total possible path we can reach a target at
            # the current index and total value
            # for example -> Let's say we are at +1+1-1 or -1+1+1 or +1-1+1 (i,total) -> (3,2)
            # We can traverse through the dfs by doing adding let's say +1+1-1"+1"-1 -> this will make 
            # a succesful path and we traverse through the dfs by doing subtracting +1+1-1"-1"+1 this will
            # also make another possible path. In this case at (3,2) adding will have 1 path and subtracting
            # will have 1 path which makes (3,2) = 1(adding) + 1(subtracting) have 2 possible path and we can
            # return this value and eventually merge up the decision tree and return all possible value at (0,0)

            # note: (3,2) might have more paths but im just giving an idea of how the algo process
            cache[(i, total)] = adding + subtracting
            # merging upwards, this is the first time visiting the current index and total values
            # So we can return the computed results back to either adding or subtracting.
            return cache[(i, total)]
        return dfs(0, 0)

