class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting takes O(nlogn) time and O(n) to go through the intervals
        # space complexity would be O(n)
        
        res = []
        intervals.sort(key = lambda i:i[0])
        res.append(intervals[0])
        
        for start, end in intervals:
            if res[-1][-1] >= start:
                res[-1][-1] = max(res[-1][-1], end)
            else:
                res.append([start, end])
                
        return res