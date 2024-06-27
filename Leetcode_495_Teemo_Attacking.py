class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        
        # Time complexity would be O(N)
        # Space complexity would be O(1)
        
        if len(timeSeries) == 0:
            return 0
        
        count = 0

        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] > duration:
                count += duration
            else:
                count += timeSeries[i+1] - timeSeries[i]
        return count + duration
            