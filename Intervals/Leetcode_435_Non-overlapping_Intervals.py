'''
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Solution:
The trick this problem is to keep track of the end value because if in a sorted
array, we want to limit the chance of having overlap with other intervals. Thus we ignore the
interval with greater end value when two intervals overlap and we simply +=1 to the res.
'''


class Solution:
    def eraseOverlapIntervals(self, intervals):

        # O(nlogn) time and O(1) space
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            # If intervals do not overlap we update the prev end to the new interval's end
            # since we are in sorted order.
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            # If two intervals overlap, we do res +=1 and update the prev end to the interval with the smaller end.
            else:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return res

                