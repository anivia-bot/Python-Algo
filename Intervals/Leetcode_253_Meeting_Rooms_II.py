class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:       

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