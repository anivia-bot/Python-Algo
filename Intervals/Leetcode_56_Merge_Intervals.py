'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Solution:
The trick of solving this problem is to sort the intervals based on the first index.
Which is where most of the time complexity is coming from.

Once we sorted the intervals, all is left is to iterate over the entire intervals from start
to finish and try to merge the last intervals that has been saved into res (its kinda like a stack 
where the last interval being inserted will be the most recent intervals). We update the
most recent intervals with the new range of min and max. If there are no overlap we simply add
the intervals into res.
'''


class Solution:
    def merge(self, intervals):
        # sorting takes O(nlogn) time and O(n) to go through the intervals
        # space complexity would be O(n)
        
        res = []
        if not intervals:
            return res
        intervals.sort(key = lambda i: i[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res