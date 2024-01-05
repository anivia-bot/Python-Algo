'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
'''
'''
Solution:
The trick for this problem is to realize heap can be used for this type of problem
Once we understand the concept of using heap, calculate all the dist from the points
using a for loop then save the distance, p1, p2 into a list and store it in another list
heapify the list that as all the value, heapify will use the first value in the list ([dist, p1, p2])
dist will be used to heapify

start popping the heap and add the points into res. k -= 1 as it will be used to stop the while loop
lets say k = 3, this will give the top 3 smallest distance to the origin.
'''

import heapq

class Solution:
    def kClosest(self, points, k):
        
        # heapify takes O(N) runtime and heap pop takes O(log(N)) and we need to execute k times
        # In that case the overall runtime would be O(N+klog(N))
        # Space complexity would be O(N) as we create the heap
        
        minheap = []
        def cal(x, y):
            ans = (x**2+y**2)**0.5
            return ans
        
        for point in points:
            x, y = point
            dist = cal(x,y)
            minheap.append([dist, x, y])
        
        heapq.heapify(minheap)
        res = []
        while k>0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k -= 1
        return res
        