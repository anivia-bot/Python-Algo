'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it 
represented by an array nums. You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
'''
'''
Solution:

'''

class Solution:
    def maxCoins(self, nums):

        # Time is O(N^3) and Space is O(N^2)

        newNums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = newNums[l - 1] * newNums[i] * newNums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]
        return dfs(1, len(newNums) - 2)