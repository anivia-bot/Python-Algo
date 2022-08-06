class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time complexity for this solution will be O(N) since we will only iterate through the array once
        # Space complexity will be O(N) as we will be storing pairs of values and index in the dictionary        
        # Since every numbers will only look for a particular match
        # For example, Input: nums = [2,7,11,15], target = 9
        # 2 can only be matched by 7, so if seven existed in the remaining array
        # Then 7 and 2 will be the correct match
        
        seen = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in seen:
                seen[diff] = i
            else:
                return [seen[nums[i]], i]