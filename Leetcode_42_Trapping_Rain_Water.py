class Solution:
    def trap(self, height: List[int]) -> int:
        # The time complexity would be O(N) and the space complexity would be O(1)
    
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0
        
        while r > l: 
            if lMax <= rMax:
                l += 1
                lMax = max(lMax, height[l])
                water = lMax - height[l]
                if water < 0:
                    continue
                else:
                    res += water
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water = rMax - height[r]
                if water < 0:
                    continue
                else:
                    res += water
        return res
                