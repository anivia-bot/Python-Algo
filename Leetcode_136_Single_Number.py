class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # O(N) time and O(1) space
        res = 0

        for num in nums:
            res = res ^ num
        return res