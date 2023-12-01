class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time O(NlogN) Space O(N)
        stonesHeap = [-s for s in stones]
        heapq.heapify(stonesHeap)

        while len(stonesHeap) > 1:
            firstStone = (-1) * heapq.heappop(stonesHeap)
            secondStone = (-1) * heapq.heappop(stonesHeap)
            if firstStone > secondStone:
                newStone = (-1) * (firstStone - secondStone)
                heapq.heappush(stonesHeap, newStone)
        
        return (-1) * stonesHeap[0] if stonesHeap else 0
                