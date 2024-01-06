class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # The time complexity would be O(n*(2^n)) as we are using a backtracking approach
        # The decision would be either include nums[i] or don't include it. That is where the 2 is for
        # nlongn for time complexity on the sorting algo can be ignore as 2^n is way bigger than that
        # Space complexity would be O((2^n)) as we store all the subsets
        res = []
        subset = []
        nums.sort()
        
        def backtrack(i):
            
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)
        backtrack(0)
        return res