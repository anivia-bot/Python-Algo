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

First you need to realize that if n-1 != edges then it means we either have a unconnected graph or
we have a cycle. If you have 5 nodes than you must only have 4 edges that connect each other. 
If you have 3 edges that means there will be a cycle connecting somewhere.

We create the adj list this way since it is a undirected graphs.
            adjList[node].append(edge)
            adjList[edge].append(node)
And nodes connected both ways.

Now you can choose to perform a BFS or DFS just to check if there are any nodes that are visited twice.
One thing I don't like a about this problem is when edge case like edges = [1] but it is actually connecting to
0 because "Given n nodes labeled from 0 to n - 1" So node 0 guarentee to exist. 
In general, just notice  n-1 != edges, create an adjList, run DFS or BFS and 
make sure start your BFS or DFS at 0 


'''

from collections import deque
class Solution:
    def validTree(self, n, edges):
        # Time and space complexity would both be O(N) => O(V + E)
        if n-1 != len(edges):
            return False
        
        adjList = {i:[] for i in range(n)}
        visited = set()
        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)
        
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                for i in range(len(q)):
                    n = q.popleft()
                    visited.add(n)
                    print(adjList[n])
                    for child in adjList[n]:
                        if child not in visited:
                            q.append(child)

        bfs(0)
        return True if len(visited) == n else False