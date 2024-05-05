class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # O(N*M) time and O(N) space
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in reversed(range(len(coins))):
            tmpDp = dp.copy()
            for a in range(1, amount + 1):
                tmpDp[a] = dp[a]
                if a - coins[c] >= 0:

                    tmpDp[a] += tmpDp[a - coins[c]]

            dp = tmpDp
        return dp[-1]