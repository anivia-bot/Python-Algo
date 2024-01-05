'''
Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any order. 
Each task is done in one unit of time. For each unit of time, 
the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period 
between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
'''
'''
Solution:
The trick is to treat each each (count of letter as heap nodes)
Since whenever we used a node it will be popped and added to a q untill 
the processing time reached
Since we want the most frequent letter to be used first, we will be implementing
max heap (make sure the turn all values to negative) 

Steps:
create a count dict and count each letters appearence, once it has been done
same the count ex: A:6, b:2 to a max heap => [-6, -2]
run a while loop if either heap or q are not empty, increase the time after each iteration
Two things to check in each iteration, first if heap has any value remaining hence, if maxHeap,

if maxHeap is not empty, increase the cnt (since we are using negative value with max heap)
if cnt eventually == 0, then we dont update the q, if its non zero then we add the current time + n
since that will be the time when that value will be avaliable again.

second thing is to check if q and q[0][1] == time, if q[0][1] == time it means we can add it back to the heap
pop left from the q and add the value back to the heap
return the time

In simple words, count each letter's appearence. create a heap based on appearnce and create a q for wait time
use a while loop untill both heap and q are empty, if heap, pop it off and add it to the q with its val and time
if q check if its time to add it back to the heap, update the time after each iteration. return time

'''
from collections import heapq, deque
class Solution:
    def leastInterval(self, tasks, n):
        # The time complexity would be O(N)
        # The space complexity would be O(N) as well
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1
                
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        
        while maxHeap or q:
            
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                qLeft = q.popleft()[0]
                heapq.heappush(maxHeap, qLeft)
        return time