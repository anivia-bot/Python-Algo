class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary Seach is a O(log(n)) solution
        # Space complexity would be O(1)
        
        l = 0
        r = len(nums) - 1
        while r >= l:
            
            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1
    