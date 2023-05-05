import heapq
class MedianFinder:
    
    # Since we are using a heap data structure, the time complexity for this algorithm would be O(log(N))
    # The space complexity would be O(N) as we need to maintain the heap data scruture
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -1 * num)
        while (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        while len(self.small) >= len(self.large) + 2:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        while len(self.large) >= len(self.small) + 2:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)  
            
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0]+self.large[0])/2
