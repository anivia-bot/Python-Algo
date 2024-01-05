'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.
Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
'''
'''
Solution:
The tricky part if the realize that this is a heap problem
The second tricky part would be converting everything into negative values
since python does not have a built-in max heap function

convert stones into a heap and set while as len(stones)>1 since we need at least 2 stones
to perform operation. if s1 == s2 we ignore, we push the difference between s1 and s2
once the while loop is over we return the last stone or no stone (return 0 if no stone)
'''

# mathematically speaking building a heap only require O(N) 
# however in this case we have 
# O(n) (heap build) + O(nlog(n)) (log(n) comes from popping and adding to the heap)
# (n comes from n operation on popping and adding)
# in sum the time complexity would be O(N) + O(NlogN) = O(nlog(n))
# the space complexity would be O(N) as it holds all the element in the heap

from collections import heapq
class Solution:
    def lastStoneWeight(self, stones):
        if not stones:
            return 0
        stones = [-1*s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -1*heapq.heappop(stones)
            s2 = -1*heapq.heappop(stones)
            
            if s1 == s2:
                continue
            elif s1 > s2:
                newStone = s1 - s2
                heapq.heappush(stones,-1*newStone)
            else:
                newStone = s2 - s1
                heapq.heappush(stones,-1*newStone)
        return -1*stones[0] if stones else 0
