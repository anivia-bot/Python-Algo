'''
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval 
starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers 
it contains, or more formally righti - lefti + 1.
You are also given an integer array queries. The answer to the jth query is the size of the smallest 
interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.
Return an array containing the answers to the queries.

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

Solution:

The concept for this problem isn't that hard. We first sort the intervals and queries.
We then interate over the queries and add ALL potential intervals from left to right.

We calculate the distance of the intervals and the end value and add it in the heap.
The reason we did this is because there might be intervals that has a tie and we want to use
the interval that is further to the left. 

We pop all intervals that will never touches the remaining queries.
We then add the queriesValue to the res dict if the heap still exisit.

'''


# Time complexity comes from sorting thus O(nlog(n)) + O(mlog(m)) from sorting the queries and intervals
# space complexity would be O(N+M) fro, maintaining the heap and res dict
import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        sortedQueries = sorted(queries)
        res = {}
        ans = []
        minHeap = []
        i = 0

        for j in range(len(sortedQueries)):
            queriesValue = sortedQueries[j]
            # i will keep increasing so we wont get duplicate intervals
            # queriesValue >= intervals[i][0] -> we add all intervals that is on the left side of the
            # queries, it does not mean the queries will be included in the intervals.
            # We are doing this simply to add all intervals to the heap and will be pop it out
            # on the next while loop if the queries is not in range of the intervals.
            while i < len(intervals) and queriesValue >= intervals[i][0]:
                l, r = intervals[i]
                gap = r - l + 1
                end = r
                heapq.heappush(minHeap, (gap, end))
                i += 1
            # popping all intervals that is not in range
            while minHeap and minHeap[0][1] < queriesValue:
                heapq.heappop(minHeap)
            if minHeap:
                res[queriesValue] = minHeap[0][0]
            else:
                res[queriesValue] = -1
        
        for q in queries:
            ans.append(res[q])
        
        return ans
        