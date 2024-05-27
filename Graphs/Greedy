# Two different approach, both runs in O(N) and O(1) space

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsub = nums[0]
        current = 0
        
        for num in nums:
            if current < 0:
                current = 0
            current += num
            maxsub = max(current, maxsub)
        return maxsub

# This is the two pointer solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        maxsub = nums[0]
        current = nums[0]
        
        while l < len(nums) and r < len(nums):
            if current < 0:
                r += 1
                l = r
                if r < len(nums):
                    current = nums[r]
                    maxsub = max(maxsub, current)
                continue
            if l == r:
                current = nums[l]
                maxsub = max(maxsub, current)
                r += 1
            else:
                current += nums[r]
                if current < 0:
                    r += 1
                    l = r
                    if r < len(nums):
                        current = nums[r]
                        maxsub = max(maxsub, current)
                    continue
                maxsub = max(maxsub , current)
                r += 1
        return maxsub
                
                