class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time complexity would be O(E*K) 
        # Space would be O(E)
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
            prices = tmpPrices
        return -1 if prices[dst] == float('inf') else prices[dst]