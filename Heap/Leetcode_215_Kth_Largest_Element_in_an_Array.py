'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
'''
'''
Solution:
First solution will be implementing a heap and pop it until the value reaches K

The second solution requires implementing a recursive quick select 
We first pick the right most value as a piviot, and left most value as p
we try to iterate through the entire array, if the nums[i] < piviot(nums[r])
then we swap p with nums[i] and we move p to the next position (essentially p is a ptr
that is ready to be swap when theres a value smaller than the piviot) 
The reason we are doing all these is because we are trying to make every value smaller 
than the piviot to be on the left side and everything bigger to be on the right side
once the swapping ends we swap the p position (this is where the value is greater than the piviot)
At this point we know that everything on the left of piviot is smaller than the piviot and 
everything on the right is greater than the piviot

We now recursivly call quick select if p > k we know that we need to search on the left side
if p < k we know k is on the right side, if p == k then we found the answer

In simple words, we either perform a heap and search for k or
we perform a quick select and recursively call quick select based on the difference 
between p and k
'''

class Solution:
    def findKthLargest(self, nums, k):

        # Time O(N) + O(klogN) space O(N)
        # numsHeap = [-num for num in nums]
        # heapq.heapify(numsHeap)

        # while k > 1:
        #     heapq.heappop(numsHeap)
        #     k -= 1

        # return numsHeap[0] * (-1)

        # O(N) time on average ex: O(N) + O(N/2) + O(N/4) + ..... = O(2N) => O(N)
        # O(N^2) time on the worst case
        # O(N) Space
        
        k = len(nums) - k
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
        return quickSelect(0, len(nums) - 1)