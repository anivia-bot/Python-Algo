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

Solution has been well commented in the following code.
'''

class Solution:
    def maxCoins(self, nums):

        # Time is O(N^3) and Space is O(N^2)
        newNums = [1] + nums + [1]
        dp = {}

        def dfs(l , r):
            # The reason we did not do l >= r is because there might be a possibility
            # When index equals (4, 4) and it is a valid input in this case it will just
            # be pointing at 8 and we proceed to get the left and right sub array to compute our dp
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            # default value as we will need it when finding the max values.
            dp[(l, r)] = 0
            for i in range(l, r+1):
                # Assume this will be the last ballon to pop, l-1 and r+1 will be the boundary
                coins = newNums[l-1] * newNums[i] * newNums[r+1]
                '''
                Going through the left subarray and right subarray and treat them as a sub problem
                And also treat them like we will pop the ballon last thus we can build up our dp cache
                For example, we know when there is only one number left the value will always be the same
                Same goes to [5,8] if we revisit -> we know if we pop these ballons last, 1 ,[5, 8], 1 the 
                the result will be the same no matter how many times we revisit as we will also keep updating the
                max value in the following line.

                How do we guarnetee it will be the max value ? When we first break it down, dfs will keep on breaking it down
                to the smallest subarray (when there is only one element left), We then slowly move it back the dfs traversal
                and compute the subarray with two elements, three element till we have the orignal array covered.
                '''
                coins += dfs(l, i-1) + dfs(i+1, r)
                # During the course of dfs the below dp[(l, r)] will change and won't always
                # be the default value (0) that we set.
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]        
        # Lets say the array is [3,1,5,8] and we want to start our dfs for index 3 and 8 
        # index one is because we added [1] + nums + [1] so we are starting at 1 and len(nums)-> (4)
        # Which makes the index 1, 4 -> maxCoins(1, 4)
        return dfs(1, len(nums))
        