'''
You are given an array points representing integer coordinates of some points on a 2D-plane, 
where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance 
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is 
exactly one simple path between any two points.
Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
'''

'''
Solution:
This solution requires Prim's Algo.
First we created an adj list. Remember to add i and j since the distance goes both ways.
Also remember to use a double for loop with range(i+1). Once the pre work is completed.
Let's begin Prim's algo.

Essentially we need to create a min heap and keep track on all the point we have visited.
we return the result when visited == len(points) since all points have been visited.
We pop from the heap and get the distance and pts (the heap will always pop the closest distance)
if the point has been visited we continue to the next loop and pop it again from the heap.
we get the value from the heap and add the distance to total then add the point to visited.
We then add all the neighbor points (adjList) into the heap by running a for loop. 
If the point has been visited we skip (continue) or else we heappush to the heap and continue the algo
untill all nodes have been visited.

'''
from collections import heapq
class Solution:
    def minCostConnectPoints(self, points):
        # Prim's algo time complexity O(N^2) and O(N) space
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0
        visited = set()
        minH = [[0,0]]
        heapq.heapify(minH)

        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return res