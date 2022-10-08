class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # The time complexity would be O(N)
        # The space complexity would be O(N) as well
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1
                
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        
        while maxHeap or q:
            
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                qLeft = q.popleft()[0]
                heapq.heappush(maxHeap, qLeft)
        return time