class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # This algo runs in O(N) time as it traverse through the entire array
        # The space compelexity would be O(1) since we didnt use any auxiliary data structure
        
        p1 = 0
        p2 = len(height)-1
        maxWater = 0
        
        while p2 > p1:
            
            if height[p1] >= height[p2]:
                maxWater = max(maxWater, height[p2]*(p2-p1))
                p2 -= 1
            
            elif height[p2] >= height[p1]:
                maxWater = max(maxWater, height[p1]*(p2-p1))
                p1 += 1
            
        return maxWater