'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.


Solution:
Think of this as a two pointers/BFS traversal range, at each iteration, we try to find out
what the left boundary and right boundary for each jumps
From example one, when we make a first jump from index 0, the range it will cover is index, 1 and 2.
If we make another jump from index 1 and 2, the max you get is from index 3 to 4 (jumping 3 steps from index 1)
If the farthest range exceed len(nums)-1 then we know there will always be a way we can reach the end.
'''

class Solution:
    def jump(self, nums):

        # O(N) solution and O(1) time

        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, nums[i] + i)
            l = r + 1
            r = far
            res += 1
        
        return res


        # O(N^2) time and O(N) space for DP solution
        # dp = [float('inf')] * len(nums)
        # dp[-1] = 0

        # for i in reversed(range(len(nums) - 1)):
        #     for j in reversed(range(nums[i] + 1)):
        #         if j + i >= len(nums):
        #             dp[i] = 1
        #             break
                
        #         if dp[j + i] < dp[i]:
        #             dp[i] = 1 + dp[j + i]
        # return dp[0] if dp[0] != float('inf') else 0
