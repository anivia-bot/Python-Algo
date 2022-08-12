class Solution:
    def climbStairs(self, n: int) -> int:
        
        # This is a Dynamic Programming solution with O(N) time complexity as we only iterate through
        # the input once.
        # O(1) space complexity as we only used two variables
        
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
        