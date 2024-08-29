'''
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and 
average greater than or equal to threshold.

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. 
All other sub-arrays of size 3 have averages less than 4 (the threshold).

Solution:
This is a sliding window problem, all you need to do is to keep track of the total sum so far
and subtract nums[l] as you are ready to slide your window to the right. Only check if the average
is >= k when the window size (r - l + 1) is at size k.

repeat the process till you find all solutions.

'''

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        
        l = 0
        r = 0
        total = 0
        res = 0

        while r < len(arr):
            total += arr[r]

            if (r - l + 1) == k:
                totalA = total / k
                if totalA >= threshold:
                    res += 1 
                total -= arr[l]
                l += 1
            r += 1
        return res
