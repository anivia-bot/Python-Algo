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
            else:
                profit = max(profit, prices[rightPtr] - prices[leftPtr])
            rightPtr += 1
        return profit