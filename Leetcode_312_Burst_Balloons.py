class Solution:
    def maxCoins(self, nums: List[int]) -> int:

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