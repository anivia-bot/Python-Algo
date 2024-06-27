class Solution:
    def removeElement(self, nums, val):
        # O(N) run time and O(1) space
        l = 0
        r = len(nums) - 1

        while r >= l:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l
