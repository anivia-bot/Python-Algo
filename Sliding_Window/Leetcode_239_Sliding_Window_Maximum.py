'''
You are given an array of integers nums, there is a sliding window of size k which is moving 
from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
'''
'''
Solution:

Fixed sliding window problem. Return maxNum * len(nums) if len(nums) < k:
ex: k = 10, nums = [1,2,3] return [3, 3, 3]

The trick is to mantain that the left most value in the q to be the largest num in k size bracket
while we shift the bracket to the right. 
Two scenarios: 
One if we encounter number that are greater than the left most value in the q:
we then pop everything from the q then we append the largest val into the q

Second, if the left pointer is now equal to the left most value. It means the next iteration
the left most value will not be included in the bracket. Thus we pop it off from the q

When we reach to the point where the string is the size of k. Left and right ptr will both + 1
otherwise we will just be expending the right ptr untill the condition is satisfied.

'''

import collections
class Solution:
    def maxSlidingWindow(self, nums, k):

        # O(N) time and space

        if len(nums) < k:
            maxNum = float('-inf')
            for i in range(nums):
                maxNum = max(maxNum, nums[i])
            return [maxNum] * len(nums)

        output = []
        q = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

            if (r - l + 1) >= k:
                output.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1

            r += 1
        return output

