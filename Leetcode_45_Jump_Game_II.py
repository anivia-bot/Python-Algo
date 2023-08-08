class Solution:
    def jump(self, nums: List[int]) -> int:

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
