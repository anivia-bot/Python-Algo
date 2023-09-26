'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 '''


'''
Solution:

The tricky part is to recognize this is a sliding window problem
Once it is recognized the problem became much simpler

First use a max function to calculate the max profit
Then update the left ptr if the right ptr is smaller 
(since we want to be buying stock at a lower price)
update the right ptr by every iteration

'''


class Solution:
    # The time complexity would be O(N) since it is a two pointer one pass solution
    # The space complexity would be O(1) since it only required 2 extra pointers for this solution
    def maxProfit(self, prices: List[int]) -> int:
        leftPtr = 0
        rightPtr = 1
        profit = 0
        
        while rightPtr < len(prices):
            profit = max(profit, prices[rightPtr] - prices[leftPtr])
            if prices[leftPtr] > prices[rightPtr]:
                leftPtr = rightPtr
            rightPtr += 1
        return profit

class Solution:
    # The time complexity would be O(N) since it is a two pointer one pass solution
    # The space complexity would be O(1) since it only requird 2 extra pointers for this solution
    def maxProfit(self, prices):
        leftPtr = 0
        rightPtr = 1
        profit = 0

        while rightPtr < len(prices):
            profit = max(profit, prices[rightPtr] - prices[leftPtr])
            if prices[leftPtr] > prices[rightPtr]:
                leftPtr = rightPtr
            else:
                profit = max(profit, prices[rightPtr] - prices[leftPtr])
            rightPtr += 1
        return profit
        