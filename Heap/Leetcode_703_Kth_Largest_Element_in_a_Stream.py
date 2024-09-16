'''
Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing 
the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
'''
'''
Solution:
The trick for this problem is just maintain the heaap with size k
use a while loop to make the heap size k
if the added value is greater than the smallest val then we pop the smallest val 
luckily min heap will automatically put the samllest at the beginning
all we need to do is the add to the heap and pop the first ele when the
heap size is greater than k
'''

from collections import heapq
class KthLargest:
    # Time O(Nlog(N)) -> creating a heap is (n-k)log(n) -> in the worst case it will just be
    # O(nlog(n)) and add or pop will just be log(n) operation
    # Space O(N)

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
    
    def add(self, val):
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)