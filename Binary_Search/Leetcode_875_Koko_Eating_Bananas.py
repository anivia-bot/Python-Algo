'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
'''
'''
Solution:
This is a great problem to implement binary search even though the problem
DID NOT MENTION SORTED !!

Careful!! Use another variable k to track what the mid value is. Since when you calculate  this input:
piles = [3,6,7,11], h = 8

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] -> The first input you will need to divide will be 5 banana per pile.
math.ceil(pile/bananaPerHr) => 3/5 + 6/5 + 7/5 + 11/5 = 1 + 2 + 2 + 3 = 8 which matched h 
However, the correct answer is 4 banana per pile. Because of it we are not allow to have 
if time == h: return time as there could be a smaller pile of banana koko could eat.

Another thing is you need to keep track all the m value (as we are not sure if l ++ or r -- will just went over the
smallest result as the previous m was the actual min value). We return m at the end since we know eventually when
l == r we found the smallest possible pile

In sum, know it is a binary search approach and only return the mid value since there could be smaller values in the pile.

Since koko's eating speed can vary from 1 banana to the max number of banana in the pile (n)
1 ~ n is sorted on its own 1,2,3,4,5,.....n
All we need to do is perform a binary search to determine if the hours spent by koko eating the
bananas will exceed h (time the guard gone for)
if the overall eating time will not exceed, r = mid - 1 so koko can eat less banana per hr
if the overall eating time will exceed the h then l = mid + 1 koko needs to eat more banana per hr
'''
import math
class Solution:
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        k = 0

        def bananaHrCount(bananaPerHr):
            hrsCount = 0
            for pile in piles:
                hrsCount += math.ceil(pile/bananaPerHr)
            return hrsCount
        
        while l <= r:
            m = (l + r) // 2
            time = bananaHrCount(m)
            if time > h:
                l = m + 1
            else:
                k = m
                r = m - 1
        return k