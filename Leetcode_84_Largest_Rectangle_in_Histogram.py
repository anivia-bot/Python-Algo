class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This algo runs in O(N) time and O(N) space
        maxArea = 0
        stack = []
        
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, (h*(idx-i)))
                start = i
            stack.append((start, height))
            
        for i, h in stack:
            maxArea = max(maxArea, (h*(len(heights)-i )))
        
        return maxArea
                