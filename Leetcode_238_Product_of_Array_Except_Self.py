class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The time complexity is O(N) and the space complexity would be O(N)
        res = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for j in reversed(range(len(nums))):
            res[j] *= post
            post *= nums[j]
        return res
        