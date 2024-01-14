class Solution:
    def countComponents(self, n, edges):
        # Time and space are both O(N) => O(V+E)
        par = [n for n in range(n)]
        rank = [1 for n in range(n)]

        def find(n):
            p = par[n]
            while p != par[p]:
                # path compression
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
            if union(n1, n2):
                n -= 1
        return n