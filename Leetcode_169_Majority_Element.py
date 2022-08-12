class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Boyer-Moore Voting Algorithm with O(N) run time and O(1) space
        
        if not nums:
            return
        
        count = 0
        highestNum = 0
        
        for num in nums:
            if count == 0:
                highestNum = num
        
            if num == highestNum:
                count += 1
            else:
                count -= 1
        return highestNum
        
        
        # This is the hashmap solution with O(N) time and space complexity
        if len(nums) == 1:
            return nums[0]
        count = {}
        majEleCountSize = len(nums)//2
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                if count[num] + 1 > majEleCountSize:
                    return num
                count[num] += 1