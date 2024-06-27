class Solution:
    def findMinHeightTrees(self, n, edges):
        # This algo runs in O(N) time and O(N) space
        graph = [set() for x in range(n)]
        for edge in edges:
            for e in edge[1:]:
                graph[edge[0]].add(e)
                graph[e].add(edge[0])
                
        q = [y for y in range(n) if len(graph[y]) < 2]
        tmp = []
        
        while True:
            for node in q:
                for n in graph[node]:
                    graph[n].remove(node)
                    if len(graph[n]) == 1:
                        tmp.append(n)
            if not tmp:
                break
            q = tmp
            tmp = []
        return q