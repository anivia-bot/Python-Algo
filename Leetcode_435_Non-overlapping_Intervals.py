class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # O(nlogn) time and O(1) space
        res = 0
        intervals.sort()
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if start >= lastEnd:
                lastEnd = end
            else:
                res += 1
                lastEnd = min(lastEnd, end)
        return res
                
                