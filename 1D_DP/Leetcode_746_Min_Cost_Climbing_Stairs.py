'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, 
you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
'''

'''
Solution:
The key to this DP problem is to start from the end and 
try to find the minium distance it could reach to the destination.
             0   1   2   3
For example [10, 15, 20] 0
The shortest path for position 2 to reach 3 is 20
The shortest path for position 1 to reach 3 is min(15, 15+20) since you can take 1 step or 2 steps
The shortest path for position 0 to reach 3 is min(10+15, 10+20) since you can take 1 step or 2 steps
Basically you try to set the minium cost for each position starting from 2 -> 0 and update the list
once every positions have the updated/minum value, we simply compare the first and second position and
return the smallest value

remember to append a 0 at position 3 so when we try to calulate from position 1 we dont go out of bounce
we start but calculating from position 1 since position 2 will always be the min steps from that position.
That's why we have the len(cost) - 2 (we add 0 + we are starting from position 1)

'''
class Solution:
    def minCostClimbingStairs(self, cost):
        # time is O(N) and space is O(1)
        cost.append(0)
        for i in reversed(range(len(cost) - 2)):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1]) 