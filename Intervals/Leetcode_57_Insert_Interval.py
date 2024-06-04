'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Solution:
The trick for this problem is to iterate over the entire intervals one by one and add the
overlapping intervals by updating newInterval using min and max function. 
In sum, all we need to do is iterate over every intervals and merge the intervals if they 
overlaps. There are two cases if the intervals does not overlap (if the interval's end is less
than the newInterval start) we simply add it to the res. If the newInterval's end is less than the
start of the current interval, we simple add the newInterval and return res + intervals[i:]
since the intervals are all in sorted order.
'''

class Solution:
    def insert(self, intervals, newInterval):
        
        # This runs in O(N) time and O(N) space        
        res = []

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append(intervals[i])
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        
        # We need this since there are case where every interval has been combine into one newInterval
        # or this newInterval has huge newInterval[0] and will be the last interval to be added to res
        res.append(newInterval)
        return res