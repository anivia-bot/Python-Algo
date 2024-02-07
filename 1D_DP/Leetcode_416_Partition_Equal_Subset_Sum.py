class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # The time complexity would be O(N*sum(nums))
        # Space complexity would be O(sum(nums))
        
        if sum(nums) % 2:
            return False
        
        dp = set()
        target = sum(nums)//2
        dp.add(0)
        
        for i in nums:
            tempSet = set()
            for j in dp:
                if (i+j) == target:
                    return True
                else:
                    tempSet.add(j+i)
                    tempSet.add(j)
            dp = tempSet
        return True if target in dp else False
        