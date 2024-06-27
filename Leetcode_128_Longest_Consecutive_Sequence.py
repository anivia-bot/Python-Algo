class Solution:
    def longestConsecutive(self, nums):
        # O(N) time and O(N) space
        numsSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numsSet:
                length = 1
                while (num + length) in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest
            