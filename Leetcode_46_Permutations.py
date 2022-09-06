class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time complexity would be O(N!)
        # Space complexity would be O(N)
        res = []
        seen = set()
        
        def backtrack(nums, curr):
            if len(nums) == len(curr):
                res.append(curr.copy())
                
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)
                    backtrack(nums,curr)
                    curr.pop()
                    seen.remove(num)
        backtrack(nums, [])
        return res