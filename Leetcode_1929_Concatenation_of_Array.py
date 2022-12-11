class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # This runs in O(N) time and O(N) space
        ans = nums + nums
        return ans