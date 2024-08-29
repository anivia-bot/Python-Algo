"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Solution:

This is bascially the same as a 3 sum problem and all you need to do is to break up the array into 3 sum and feed it
into a 3 sum function, the rest of the algo would be exactly the same as 3 sum. Care for edge cases just like 
3 sum where you are not allow to have repeated values for the first number and you are not allow to have repeated
values for the second number.
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []

        def threeSum(smallNums, target):
            res = []
            for i in range(len(smallNums)):
                if i > 0 and smallNums[i-1] == smallNums[i]:
                    continue
                left = i + 1
                right = len(smallNums) - 1
                while left < right:
                    total = smallNums[i] + smallNums[left] + smallNums[right]
                    if total == target:
                        res.append([smallNums[i], smallNums[left], smallNums[right]])
                        left += 1
                        while left < right and smallNums[left] == smallNums[left - 1]:
                            left += 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1

            return False if not res else res

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            firstNum = nums[i] 
            remainingSum = target - firstNum
            remaingNums = threeSum(nums[i+1:], remainingSum)
            if i < len(nums) - 3 and remaingNums:
                for arr in remaingNums:
                    res.append([nums[i], arr[0], arr[1], arr[2]])
            
        return res