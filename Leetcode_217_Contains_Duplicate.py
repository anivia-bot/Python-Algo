class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time complexity would be O(N)
        # Space complexity would be O(N) as well
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False
        