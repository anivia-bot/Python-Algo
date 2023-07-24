class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time and space are both O(N) => O(V+E)
        par = [i for i in range(n)]
        rank = [1] * n
        res = n

        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res