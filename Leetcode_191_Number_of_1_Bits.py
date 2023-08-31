class Solution:
    def hammingWeight(self, n: int) -> int:

        # O(32) time -> O(1) time and O(1) space
        res = 0
        while n != 0:
            res += n % 2 
            n = n >> 1
        return res