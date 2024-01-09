'''
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
'''     
'''
Solution:
The key for this is to map the old node as key and new node as value
        {
        old1: New1,
        old2: New2
        }
and use a DFS to traverse through all the node and add it to the
new nodes neighbor

The algo goes as, if the old node is in the hash map
return the newNode, if its not in the hash map which means
this node has never been visited, create a new node and add it to the
hash map, iterate through the old nodes neighbors and add it to the 
newNodes's with DFS
'''

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    # This algo runs in O(N) time and O(N) space
    def cloneGraph(self, node):
        if not node:
            return None

        cloneDict = {}
        def dfs(node):
            if not node:
                return
            if node in cloneDict:
                return cloneDict[node]
            newNode = Node(node.val)
            cloneDict[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode
        return dfs(node)