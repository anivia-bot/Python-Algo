class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time complexity would be O(N) and space complexity would be O(1)
        dp = [False] * len(nums)
        dp[-1] = True
        goal = len(nums) - 1

        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i >= goal:
                dp[i] = dp[goal]
                goal = i

        return dp[0]