class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algo time complexity O(N^2) and O(N) space
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0
        visited = set()
        minH = [[0,0]]
        heapq.heapify(minH)

        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return res