class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time and space complexity would both be O(N) => O(V + E)
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
            