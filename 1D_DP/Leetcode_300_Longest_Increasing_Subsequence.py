'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''
'''
Solution:
This is another classic DP problem. Essentially we do a bottom-up dynamic programming approach.
The reason that the algo runs in O(n^2) is because it not only start from the last element that iterate
forward. We also need to check any number i+1, i+2 ... index which makes a double loop.
For example:
  0 1 2 3 4 5  6  7
[10,9,2,5,3,7,101,18]

lets say we are currently at index 4, we need to check whats the longest path index 5 (i+1) can make.
same logic we also need to check for index 6 (i+2) and index 7 (i+3) to see what is the max increasing
order at that position. This logic basically means the following line where j values starts from i+1 and 
goes all the way to the last element in the array.

if nums[i] < nums[j]:
    dp[i] = max(dp[i], 1+dp[j])

Finally, we can just simply return the largest element in the array.
We have a double for loop that cost O(n^2) and a max function at the end
which is O(n). This O(n^2) + O(n) = O(n^2)
'''


class Solution:
    def lengthOfLIS(self, nums):

        # O(N^2) time and O(N) space
        dp = [1] * len(nums)
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)