import heapq

minheap = []

minheap.append([100,3,4])
minheap.append([10,3,4])
minheap.append([9,30000000000,4])
minheap.append([8,3,4])
minheap.append([24,3,4])


heapq.heapify(minheap)

pop = heapq.heappop(minheap)
print(pop)