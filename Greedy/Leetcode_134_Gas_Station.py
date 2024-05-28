'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel 
from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel 
around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, 
it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.


Solution:
Two things you need to notice when doing this problem. First, you need to realize that
if the sum of gas is < sum of cost we will never be able to complete the circuit. Why is that? 
Since we are starting with 0 gas and there will be cost at each index, that's why the total sum
of gas has to be > the sum of cost. This will guarantee we have a solution for example, we have 
have a gas station that starts with 99, 1, 1, 1, 1, now matter what cost we have for the roads we,
will always be able to find the best solution since our gas will be cumulative.

The second thing is to realize we need to iterate over the entire array to determine which position
to start. We want the first index when the currGas gets positive. So that when we calculated a negative currGas value
i + 1 will be the first positive index. The reason we need to check the entire array is because you could get 
a first the following example shows the first index to have positive value, but later on we are not able
to find a solution to the remaining cost.
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
Output: 0   Expected:4
'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        # O(N) time and O(1) space
        if sum(gas) < sum(cost):
            return -1
        
        currGas = 0
        start = 0
        for i in range(len(gas)):
            currGas = currGas + (gas[i] - cost[i])
            if currGas < 0:
                currGas = 0
                start = i + 1
        return start 