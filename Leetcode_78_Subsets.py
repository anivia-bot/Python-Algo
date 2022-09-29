class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # The time complexity would be O(n*(2^n)) as we are using a backtracking approach
        # The decision would be either include nums[i] or don't include it. That is where the 2 is coming from.
        # Space complexity would be O((2^n)) as we store all the subsets

        res = []        
        subset = []

        def dfs(i):
            
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res