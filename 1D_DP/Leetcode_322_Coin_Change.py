'''
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
'''
'''
Solution:

'''
class Solution:
    def coinChange(self, coins, amount):
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
        