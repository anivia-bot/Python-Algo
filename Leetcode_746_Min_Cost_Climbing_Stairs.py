class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # time is O(N) and space is O(1)
        cost.append(0)
        for i in reversed(range(len(cost) - 3)):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1]) 