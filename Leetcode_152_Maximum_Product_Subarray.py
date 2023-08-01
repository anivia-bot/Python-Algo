class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(N) time and O(1) space

        res = max(nums)
        currentMax = 1
        currentMin = 1

        for num in nums:
            tmpMax = num * currentMax
            currentMax = max(num * currentMax, num * currentMin, num)
            currentMin = min(tmpMax, num * currentMin, num)
            res = max(currentMax, res)

        return res