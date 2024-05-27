'''
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Solution:

The trick for this problem is to use a DP array and update the goal to be closer 
whenever we find a match. For example, at first we need to reach the last index (4) to
reach the goal, if we now find out that index (3) are also able to reach to goal then we 
can simple set our goal to be at index (3) since we know if we ever reached index (3) we 
will be able to find a path to the last index. 

Basically we use a bottom-up DP approach with a little bit of twist by moving the goal
closer when we find a match. This saves some time on the time complexity part as we 
don't need a double for loop to find out any future dp index has a match.

'''


class Solution:
    def canJump(self, nums):
        # Time complexity would be O(N) and space complexity would be O(1)
        dp = [False]*len(nums)
        dp[-1] = True
        goal = len(nums)-1

        for i in reversed(range(len(nums)-1)):
            num = nums[i]
            if num + i >= goal:
                dp[i] = True
                goal = i

        return dp[0]
            