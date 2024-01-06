'''
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. 
Answers within 10-5 of the actual answer will be accepted.
Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''
'''
Solution:
The easiest way to solve this problem is to split two lists into maxHeap and minHeap
Once the two heap is balanced, we just retrieve the first value from both maxHeap and minHeap
and calculate the median (if two heaps are equall length)

First initalize samll and large array and heapify them. Once both heaps have been created.
We can start pushing values into it. Our default will be pushing value into the small heap
then we run a balance function to make sure the heap will maintain a heap properity.
Finally since the heap property has been maintain, all we need to do is to check the length 
of both heap (len diff should be within 1) if there's a diff more than one, just pop the longer 
heap and add it to the shorter heap, remember to multiply -1 when getting value from the small heap
since it is a maxHeap (python need to multiply -1)

Once we can guarentee two heap are balanced and their len are with +- 1 then we can just retrieve vals
from the heap and return the median.


'''
import heapq
class MedianFinder:
    
    # Since we are using a heap data structure, the time complexity for this algorithm would be O(log(N))
    # The space complexity would be O(N) as we need to maintain the heap data scruture
    def __init__(self):
        self.small = []
        self.large = []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def balance(self):
        while self.small and self.large and ((-1*self.small[0]) > self.large[0]):
            smallVal = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, smallVal)

    def addNum(self, num):
        heapq.heappush(self.small, -1*num)
        self.balance()
        while len(self.small) > len(self.large) + 1:
            smallVal = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, smallVal)
            
        while len(self.large) > len(self.small) + 1:
            largeVal = -1*heapq.heappop(self.large)
            heapq.heappush(self.small, largeVal) 

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0]) / 2