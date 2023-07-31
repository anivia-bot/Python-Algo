class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(N) time and O(1) space

        if not nums:
            return 0

        rob = 0
        robnext = 0
        

        for i in range(len(nums)):
            tmp = max(nums[i] + rob, robnext)
            rob = robnext
            robnext = tmp
        return robnext
