'''
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] 
indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from 
src to dst with at most k stops. If there is no such route, return -1.
Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
'''
'''
Solution:
This is a classic bellman ford algo which can also be solved by BFS
We provided both BFS and bellman ford solution.
The bellman ford solution basically we need to set all nodes to be
positive infinity except the starting node to be 0. We then iterate
over k+1 times (since direct flight is 0 stops). We set a tmp variable with the copy of res is because
for s, d, p in flights: will go over every node including the stop nodes
       400
ex:  1 --> 3
100 /     /
   2------
     100
    In this case 1 -> 2 -> 3 , 2 is the stop node and 
    Let's say k is 0 (only want direct flight) if we dont have a tmp we will then mark
    desitnation node to be 200 since we will iterate over all nodes and update res inplace.
    That's why we need a tmp and a if statement to skip nodes if the node is currently infinity

We then update the tmp and update res at the end of the for loop. Peform this operation
k+1 time and we will have the result. resturn -1 if dst is infinity (means it cant be reached)
else return the dst value
    
'''


from collections import deque
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Time complexity would be O(E*K) 
        # Space would be O(E)
        adjList = {}
        for f, t, p in flights:
            if f not in adjList:
                adjList[f] = []
            if t not in adjList:
                adjList[t] = []
            adjList[f].append([t, p])
        res = float('inf')
        q = deque()
        nodeMap = [float('inf') for _ in range(n)]
        count = 0
        for t, p in adjList[src]:
            q.append([t, p])

        while q and count < k+1:
            for i in range(len(q)):
                node, p = q.popleft()
                if node == dst:
                    res = min(p, res)
                    continue
                if p > nodeMap[node] or p > res:
                    continue
                for nei in adjList[node]:
                    d = nei[0]
                    price = nei[1]
                    if p > nodeMap[d]:
                        continue
                    q.append([d, p+price])
            count += 1
        return -1 if res == float('inf') else res
    
# Solution with bellman ford
        res = [float('inf')] * n
        res[src] = 0

        for i in range(k+1):
            tmp = res.copy()
            for s, d, p in flights:
                if res[s] == float('inf'):
                    continue
                if res[s] + p < tmp[d]:
                    tmp[d] = res[s] + p
            res = tmp
        
        return -1 if res[dst] == float('inf') else res[dst]