class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # This DP solution will runs in O(amount * coins) time or O(N*M)
        # since it will iterate through a next for loop
        # The space complexity would be O(N) as we store the coins dp array
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        for a in range(amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
                    
        return dp[-1] if dp[-1] < (amount+1) else -1
        