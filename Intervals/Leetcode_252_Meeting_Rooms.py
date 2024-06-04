class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #O(nlogn) time and O(1) space

        intervals.sort()
        if not intervals:
            return True
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if lastEnd > start:
                return False
            else:
                lastEnd = max(lastEnd, end)

        return True