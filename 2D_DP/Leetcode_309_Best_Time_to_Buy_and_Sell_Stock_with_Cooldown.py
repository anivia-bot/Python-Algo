'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Solution:

To me this is a very hard DP problem to wrap my head around,
In sum, we need to create an dp dictionary and store all buyingStatus in the 
dictionary. For example, dp =   {
                                    (4,False "sell" ):2
                                    (3,True "buy" ):2
                                }
means if you sell at the 4th position, the max profit you will get is 2,
vice versa, if you buy at the 3rd position, the max profit you will get is 2

Remeber!! (4,False "sell" ):2 for all sell's key, they only store the NET PROFIT
from the sell, what does that mean? it means if you sell at $6, $10, $14 your
total net profit will be $30 and you will have to subtract your buying price at the end when 
we iterate back to this line     

if buying:
    buy = dfs(i + 1, False) - prices[i]

since dfs(i + 1, False) will go to sell and we subtrack the prices at the current buying price (price[i])

Essentially, you create a dp hashmap that pass in the state of and index as key and the max profit as 
the value. If we ever visited the dp we return the max profit at that index and if it goes out of bounce
we return 0 since if the stock price goes as 5,4,3,2,1 it will be better if we dont buy at all and proceed to 
execute this line coolDown = dfs(i + 1, buying) recursively. 

If we are in a buying state(True) we have 2 option, i+1 then sell(False) and cooldown and continue to the next index.
Same goes for selling state except we perform an i+2 then buy(True) and cooldown and continue to the next index.
return dp[i, buying] since dfs will iterate to the end of the index (kinda like a bottom up DP approach). Once 
all the iterate is completed, the dp map will be filled and the first index will tell us what is the max combination
since we can choose either buying at the first index or skip the first index and do a cool down. Plus we use a 
bottom up DP approach so we can guarentee that the returned result will be the max possible outcome.
'''

class Solution:
    def maxProfit(self, prices):

        dp = {}

        def dfs(i, buying):
            # base case when goes out of bounce
            if i >= len(prices):
                return 0
            # if we revist a index we computed, just return.
            # we are using bottom-up so it will be the best possible result
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # if we are buying there are 2 options
                # First option is we sell at the next index. and we subtract the net profit
                buy = dfs(i + 1, False) - prices[i]
                # We are not buying at the current index
                coolDown = dfs(i + 1, buying)
                # storing the max profit outcome between buy and no buy
                dp[(i, buying)] = max(buy, coolDown)

            else:
                # We sold at this index price[i] and add all possible future sold index
                sell = dfs(i + 2, True) + prices[i]
                # We do NOT sell and move to the next index.
                coolDown = dfs(i + 1, buying)
                # storing the max profit outcome between sell and no sell
                dp[(i, buying)] = max(sell, coolDown)

            # return the max we could get at the current index (the if else statement 
            # should took care of it)
            return dp[i, buying]
        # Starting the dfs from the first index and set it as a buying state
        dfs(0, True)
        # return the result from the first index.
        return dp[(0, True)]

            