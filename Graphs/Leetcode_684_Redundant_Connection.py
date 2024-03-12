'''
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.

Example 1:
o
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
'''
'''
Solution:
This isn't the usual graph problem. This includes Union-Find algo and path compression.
For the is type of problem you need a list of all the par and rank for each nodes
The union function will first find the parents of n1 and n2. if the for the first time
the the parents are the same which means their is already a path that can connect to their 
parents, hence a redundant connection. So lets say[1,3], [1,2] => 3 -- 1 -- 2 This is fine so far
untill we add another edge [3, 1] then at this point we will notice that 3, 1 have the same parent
and p1 == p2 and we return the redundant connection immediately.

If the parents are not equal. we need to union them together base on rank.
for example: [2,3] node 2 has 4 rank and node 3 has 1 rank (node 3 will be a child of node 2)
and we change node 3's parent to be node 2

Now lets teckle on the find method. We first set p to the parent of the node
we run a while loop that check if p != par[p] lets say p is now 2 and par[2] is also 2
then we know we reached the end of the iteration

if we have found/reach the end of the iteration. we set p = par[p] (the parent of the current p)
And a bonus operation will be including path compression by doing par[p] = par[par[p]]
This path compression basically mark the curr p's parent to something 2 steps up the tree and mark all
path p has been travese through with the need parent value. This makes the next iteration much quicker
Iterate through the edges and return the last edges when they both share the same parents

In simple words: 

Their parents are all 1 BUT if we try to make connections lets say between [2, 4] we will find out that
their parents are both 1 and thus it is a redundant connection.

The algo starts by initalizing parents to be its own and set all ranks to be 1
Then we iterate over all the edges (at this point all parents are still themselves) and 
we start assigning the smaller rank to a new parent We can do this because these 2 nodes are
already connected [1, 2] we are now just making 1 the parents of 2. Even if we assign 2 as the parent
The rank will eventually merge every possible link to make 2 the biggest parent.

The algo are quite simple as we try to find the node's parents, if the are different we union them to make
one of the nodes a parent of the other and update the rank.

dont forget to apply path compression on the find function.

    1
   / \
 2    4
  \    \
   3    5
'''
class Solution:
    def findRedundantConnection(self, edges):
        # time is O(N) and space is O(N)
        par = [n for n in range(len(edges) + 1)]
        rank = [1 for n in range(len(edges) + 1)]
        res = []
        def find(node):
            p = par[node]
            while p != par[p]:
                # this line is for path compression, this will shorten this time when
                # we search it next time
                par[p] = par[par[p]]
                p = par[p]
            return p
                                                                                                
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                res.append([n1, n2])
    
        return res[-1] if res else []
