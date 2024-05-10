'''
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any 
combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Solution:

This is a classic 2D DP problem. On the bright side we can reduce the space complexity 
to O(N) using just 2 arrays to track all the computed values. In sum, we are iterating 
the 2D array from the bottom left to the upper right corner and we are getting value from
the bottom and left since we are performing amount - coin (it will be much easier if our
base case to be set at the 0th index (amount = 0)). If we set our base case to be at the 
last index [0,0,0,0,0,1] when we do amount - coin -> 0 it will be quite complicate to do
if amount-coin == 0:
    newDp[amount] = newDp[amount+1]
or something along the line (the code will get really messy)

'''

class Solution:
    def change(self, amount, coins):

        # O(N*M) time and O(N) space
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in reversed(coins):
            # Crearing a tmp array since we only need two array to track
            # Our dp progression and that makes our space complexity to be O(N)
            newDp = [0] * (amount + 1)
            newDp[0] = 1

            # We did not iterate in reverse is because when we do (a - coin)
            # amount 5 - coin(5) = 0 It will be much easier to set the 0th
            # index to be our base case [1,0,0,0,0,0]
            # Normally when we do a bottom-up DP approach we will take the
            # value from the bottom and the right, however in this case 
            # it will be much easier to do bottom and left because we are
            # utilizing index to be the ammount 

            # ex: ammount (5) - coin (5) = index (0) base case which also
            # has a default value of 1 which means there is one solution
            # for coin 5 at ammount 5
            for a in range(1, amount+1):
                # This is basically getting value from the bottom array
                # Let's say we are at coin 1, when we trying to get the value
                # from the bottom array, which means getting all the possible 
                # combinations from both coin 2 and coin 5.
                newDp[a] = dp[a]
                if a - coin >= 0:
                    # Try to check to the left and see if there are any possible
                    # ways that we can form a result with the current coin value.
                    newDp[a] += newDp[a-coin]
            # update dp with newDp and repeat untill we are iterating over the last coin
            dp = newDp
        # since we are getting value from bottom-left, when we finish the array, the last
        # value will be on the upper right corner.
        return dp[-1]