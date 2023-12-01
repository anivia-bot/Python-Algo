class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

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