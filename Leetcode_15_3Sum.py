class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # For the algo, the sorting part will take at least nlog(n) time and 
        # the two pointer approach in a nested loop will take O(n^2) time so in total it would be O(n^2)
        # Space complexity would take a O(N) or O(1) depends on the result or sorting algo

        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while r > l:
                total = nums[l]+nums[r]+nums[i]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while r > l and nums[l] == nums[l-1]:
                        l += 1
        return res
                    