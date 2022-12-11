class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # The time complexity would be O(N) and the space complexity would be O(1)
        count = 0
        firstNum = None
        insertIdx = 1
        for i in range(len(nums)):
            if i == 0:
                firstNum = nums[i]
                continue
            if nums[i] == firstNum:
                count += 1
                firstNum = nums[i]
            elif nums[i] != nums[i-1]:
                nums[insertIdx] = nums[i]
                firstNum = nums[i]
                insertIdx += 1
        return len(nums) - count

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         size = len(nums)
#         insertIndex = 1
#         for i in range(1, size):
#             # Found unique element
#             if nums[i - 1] != nums[i]:      
#                 # Updating insertIndex in our main array
#                 nums[insertIndex] = nums[i] 
#                 # Incrementing insertIndex count by 1 
#                 insertIndex = insertIndex + 1     
#         return insertIndex