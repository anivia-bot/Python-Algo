'''
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all 
meetings to their schedule without any conflicts.

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30),(5,10) and (0,30),(15,20) will conflict

Solution:

The trick for this problem is to sort the intervals based on the starting index and interate over the
intervals, return False when there's an overlapping time. We keep track of the end time and update it
to the max end time since all meeting are non overlap and can not be canceled.
'''



class Solution:
    def canAttendMeetings(self, intervals):
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