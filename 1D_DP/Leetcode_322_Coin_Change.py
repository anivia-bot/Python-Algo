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
This is a classic DP problem, the difference for this problem then other DP is
that other DP problem can just track 2 variables, they are not trying find acumulated
steps, for example, other DP problem ex: climbing staris, you can choose to jump one step
or two steps, that why it is easy to just track the two variable. Let's say you can either start
from step 0 or step 1 then all you need to do is the run the algo twice with different index.

For this problem we need to create a dp array fills with inf values, (if we find a smaller val 
we then replace the inf value) the first for loop is the fill the cost for number 1 ~ number amount.
Ex: how much coin does it need to fill amount 1 ? 1 coin.

The second for loop is to iterate over the coins to see if there is a way to find the
the least coin needed to fill at that specific amount. Ex: lets say we have a coin with
a value of 2, amount 4 will be 1 + dp[4-2], the 1 in this case represent one coin with a value
of 2 that has been used. Then we check the value at dp[4-2] = dp[2] and try to find the smallest
possible value from dp[2]

In sum, we start a dp array fill with inf, we run dp on amount then calculate all the coins
needed for every amount. We then iterate over all the coins and see if there is any coins 
can form a smaller values. Of course the condition is when the amount is greater than the coins.
Ex: amount 1 we cant use a 3 coin cuz it will be negative. If the amount is positive.
Save the min of the current dp[a] amount or 1+[a-c].

return the last amount from the dp list, if the last amount is still inf then we just simply
return -1 as there is no possible ways to create the combination.
'''
class Solution:
    def coinChange(self, coins, amount):
        # This DP solution will runs in O(amount * coins) time or O(N*M)
        # since it will iterate through a next for loop
        # The space complexity would be O(N) as we store the coins dp array
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for a in range(amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
                    
        return dp[-1] if dp[-1] < (amount+1) else -1
        