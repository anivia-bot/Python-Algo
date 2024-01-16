'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] 
represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". 
If there are multiple valid itineraries, you should return the itinerary that has the 
smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
'''
'''
Solution:
Hard problem with many edge case to take care of.
Since there might be multiple path and we need to return with the smallest lexical order.
That's why we sort tickets before we build our adj list. rmbr to add dst with [] since
that might be our first base case if it can't be reach by any values

Once we built our adj list all we need to do is perform a special form of DFS as DFS 
will traverse to the very end(destination which will be the destination with no 
more destination to go) + the adj list is sorted. We utilize a while loop to check
if adj[airport] is empty or not. if its empty then it means it reaches the end. Thus
we add the current airport into our result. we repeat this process untill all nodes are visited.
rembr to return a reversed res since add the last airport first.

In sum, sort tickets, make adj list with dst included, dfs with while loop to check if 
the list of adj[airport] is empty. If its empty we reached the end of dfs (since it can not ever be 
reach (it doesnt loop back to other airports) so we put this at the very end)
return the reversed res as we are guarenteed a path.
'''
class Solution:
    def findItinerary(self, tickets):
        # Time complexity would be O(V+E)^2
        # Space complexity would be O(v + E)
        adj = {}
        tickets.sort()
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
        res = []

        def dfs(airport):
            while adj[airport]:
                ap = adj[airport].pop(0)
                dfs(ap)
            res.append(airport)
        dfs('JFK')
        res = reversed(res)
        return res