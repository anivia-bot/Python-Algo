class Solution:
    def sortColors(self, nums):
        """
        Perform a bucket sort with one-pass solution that runs in O(N) solution and O(1) time
        Look out for edge case when swaping 0 with the right ptr
        """
        
        leftPtr = 0
        rightPtr = len(nums) - 1
        i = 0
        
        def swap(l, r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
        
        while rightPtr >= i:
            if nums[i] == 0:
                swap(leftPtr, i)
                leftPtr += 1
            elif nums[i] == 2:
                swap(i, rightPtr)
                rightPtr -= 1
                continue
            
            i += 1
        return nums
                