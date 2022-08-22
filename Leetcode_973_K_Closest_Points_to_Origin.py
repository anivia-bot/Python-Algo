import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # heapify takes O(N) runtime and heap pop takes O(log(N)) and we need to execute k times
        # In that case the overall runtime would be O(N+klog(N))
        # Space complexity would be O(N) as we create the heap
        
        minheap = []
        def cal(x, y):
            ans = (x**2+y**2)**0.5
            return ans
        
        for point in points:
            x, y = point
            dist = cal(x,y)
            minheap.append([dist, x, y])
        
        heapq.heapify(minheap)
        res = []
        while k>0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k -= 1
        return res
        