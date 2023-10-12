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
        l, r = 1, max(piles)
        minHr = float('inf')

        while l <= r:
            
            mid = (l + r) // 2
            hrSpent = 0
            for pile in piles:
                hrSpent += math.ceil(pile/mid)
            
            if hrSpent <= h:
                minHr = min(minHr, mid)
                r = mid - 1
            else:
                l = mid + 1
        return minHr
