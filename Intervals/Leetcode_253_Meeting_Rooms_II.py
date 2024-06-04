'''
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days 
required to schedule all meetings without any conflicts.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Solution:

The trick for this problem is to create two sorted list of start time and end time.
If the start time is less than the end time we know there is an meeting that is on going.
We are always comparing the earliest meeting end time with the earilest start time since we sorted the array.

If the start time < end time we know there are a meeting that is ongoing and we do a +=1 on the count then
we move to the next start time. If the next start time is also less than the current end time
we do another +=1 on the count which also means we need 2 days to fit all meetings.
We use a res = max(count, res) to track the max value of meetings at one point
We also need to decriment -= 1 then a meeting ends, hence when the start time > end time. In this case we do a -=1
on the count and move to the next end time.

Ex:

Start = [0, 5, 10]
End =   [10, 15, 30]

We increase the count when the end time is greater than the start time. we then update the
res = max(res, cnt) Then we move to the next start time. If the start time is still less then 
the end time. We increase the count again and update the res. If the end time is now less than or 
equal to the start time that means a meeting is over and we decrease the count. Since we kept checking
res = max(res, cnt) at each iteration we can get the max cnt at one point and that will be our solution

'''


class Solution:
    def minMeetingRooms(self, intervals):       

        # O(nlogn) time and O(n) space 
        
        startTime = []
        endTime = []
        res = 0
        cnt = 0
        s = 0
        e = 0
        for i in intervals:
            startTime.append(i[0])
            endTime.append(i[1])

        startTime.sort()
        endTime.sort()

        while s < len(intervals):
            if startTime[s] < endTime[e]:
                cnt += 1
                s += 1
            else:
                cnt -= 1
                e += 1
            res = max(res,cnt)
        return res