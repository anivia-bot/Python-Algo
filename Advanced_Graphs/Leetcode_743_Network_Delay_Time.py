'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, 
vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.
Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
'''
'''
Solution:
This is Djikstra Algo which is very similar to Prim's algo
Djiksta utalize min heap to pop the current shortest path element.
DO NOT think of it as a deque, the order of us adding to the heap does NOT matter.
All we care is the distance that we are on currently. We continuously increase the
path distance and add it to the heap. -> Because of it, we don't have to worry that if
there are other path that might have a shortcut to our target node since min heap will be
popping off the smallest path and we will always be processing the shortest/closest node first.

In sum, we create adj list for all nodes (node and nei) since there might be node that arent connecting
to any other nodes. Create a visited hashset and min heap with value 0 and kth node inserted and set 
time to -1. Since if we cant visit every node we will just return -1.

Start our while loop with if minH, and start popping off the element. If we seen the node then we skip it (continue),
if not we add it to visited and check if visited == n, since if we visited all the nodes we can simply return the time.
if we havent visted all the nodes then we just iterate over the current node's nei and add it to the q
remeber the add the current path + the nei time in order the correctly sort through the heap.
'''

from collections import heapq, collections
class Solution:
    def networkDelayTime(self, times, n,k):
        # O(N + ElogN) time and O(N + E)
        adjList = {}
        for node, nei, time in times:
            if node not in adjList:
                adjList[node] = []
            if nei not in adjList:
                adjList[nei] = []
            adjList[node].append([time, nei])

        minH = [[0, k]]
        heapq.heapify(minH)
        visited = set()
        totalTime = -1

        while minH:
            time, node = heapq.heappop(minH)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                totalTime = time
            for t, nei in adjList[node]:
                if nei in visited:
                    continue
                heapq.heappush(minH, [t+time, nei])
        return totalTime

