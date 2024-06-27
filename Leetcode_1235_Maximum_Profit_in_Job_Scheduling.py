class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        
        # pass the decorator it is pre defined
        def lru_cache():
            pass
        # This algo runs in O(N^2) time and O(N^2) space
        n = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        print(jobs)
        
        @lru_cache(None)
        def rec(i):
            if i == n:
                return 0
            j=i+1
            while j<n:
                if jobs[i][1] > jobs[j][0]:
                    j+=1
                else:
                    break
            one = jobs[i][2] + rec(j)
            two = rec(i+1)
            return max(one,two)
        return rec(0)