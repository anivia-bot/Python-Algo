class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # O(N) time O(1) space
        
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res