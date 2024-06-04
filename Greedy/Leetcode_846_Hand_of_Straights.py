'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of 
size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, 
return true if she can rearrange the cards, or false otherwise.
Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Solution:
This problem relies on having count of how many numbers are remaining by using a dict
and another heap to keep track of the min value so that we know when to start finding
the consecutive number of hands.

We iterate over the smallest value in the heap/hand and do first, first+groupSize since
we are finding a consecutive hand. If the val is not in hashMap or we used all the count
for that number then we know we are not able to make a consecutive hand thus we return False.
Return True after we pop all numbers in the q as we used all possible numbers and there are
nothing remains.
'''


import heapq
class Solution:
    def isNStraightHand(self, hand, groupSize):

        # nlog(n) time and O(n) space
        if len(hand)%groupSize>0:
            return False
        hashMap = {}
        for h in hand:
            if h not in hashMap:
                hashMap[h] = 1
                continue
            hashMap[h] += 1
        
        h = list(set(hand))
        heapq.heapify(h)
        while h:
            first = h[0]
            for val in range(first, first+groupSize):
                if val not in hashMap:
                    return False
                if hashMap[val] == 0:
                    return False
                hashMap[val] -= 1

                # this if statement is the tricky part, If we used all the count at this particular val
                # let's say val(3) has 0 count left, and 3 is not the smallest val in the heap. That means
                # there is still a smaller value with in the groupSize let's say [2,3,4]. This means 2 still 
                # remain at least once and at one point we need to burn 2 and try to make a consecutive hand.
                # 3 is no longer there and this will meant to fail in the future that's why we return False
                # We don't have to worry that 2 might be the last value in the group and we can still possibly
                # make it work since heap[0] ALWAYS gives the samllest value in the list.
                if hashMap[val] == 0:
                    if val != h[0]:
                        return False
                    heapq.heappop(h)
        return True
    
    