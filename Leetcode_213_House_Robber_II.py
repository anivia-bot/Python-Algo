class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time is O(N) and space is O(1)

        def helper(numsArray):
            if not numsArray:
                return 0

            rob1 = 0
            rob2 = 0

            for num in numsArray:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2

        if not nums:
            return 0
        oneRob = nums[0]
        withoutFirstRob = helper(nums[1:])
        withFirstRob = helper(nums[:-1])
        return max(oneRob, withoutFirstRob, withFirstRob)
