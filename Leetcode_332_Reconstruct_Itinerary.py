class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Time complexity would be O(V+E)^2
        # Space complexity would be O(v + E)
        adj = { src:[] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = []
        res.append('JFK')
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            tmp = list(adj[src])
            for idx, val in enumerate(tmp):
                adj[src].pop(idx)
                res.append(val)
                if dfs(val): 
                    return True
                adj[src].insert(idx, val)
                res.pop()
            return False
        dfs('JFK')
        return res