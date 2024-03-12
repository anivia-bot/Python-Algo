'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.
Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
true
'''

'''
Solution:
To solve this problem you need to recognize two thing.
First tree doesnt have loop and cant have seperate graphs/trees (all nodes should be 
used in the tree)

The approach will be creating an adjlist and run a DFS on all its neighbors, one thing
you need to be careful is that you might be running dfs back to where you came from since 
the adj list will contain both val ex: 0:[1,2,3], 1:[0,1,2] as we iterate through each node's
neighbor the below edge case might occur
0---dfs--->1---dfs--->0 and this will cause problem since 0 has already been visited.

use the if not dfs(node, prev): return False when you found a value that has been visited.
Keep track of how dfs you ran since if you ran dfs more than once means you have a disjointed graphs.
'''


class Solution:
    def validTree(self, n, edges):
        # Time and space complexity would both be O(N) => O(V + E)
        if not edges:
            return True
        seen = set()
        adjList = {}
        cnt = 0

        for n1, n2 in edges:
            if n1 not in adjList:
                adjList[n1] = []
            if n2 not in adjList:
                adjList[n2] = []   
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for val in adjList[node]:
                if val == prev:
                    continue
                if not dfs(val, node):
                    return False
            return True

        for val in adjList.keys():
            if val in seen:
                continue
            if not dfs(val, -1):
                return False  
            cnt += 1          
        return False if cnt > 1 else True