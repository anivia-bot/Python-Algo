'''
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] 
describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the 
triplet you want to obtain.
To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] 
to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] 
will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.


Solution:
The trick for this problem is to ignore the any triplet that has value that are greater 
than the target triplet for example [1,8,4] and target [2,7,5] since we are taking the max
value at every index, we will never be able to make the target triplet
if we choose the max value of the middle value (8). 

The remaining will be quite easy as we just have to add the matching value and store its index.
if the stored index == to the len target values. We know we could find a match.
'''

class Solution:
    def mergeTriplets(self, triplets, target):
        
        # O(N) time and space
        matchedIdx = set()
        
        def missMatch(t):
            for i in range(len(t)):
                if t[i] > target[i]:
                    return True
            return False
        
        def matchCheck(t):
            for i in range(len(t)):
                if i in matchedIdx:
                    continue
                if t[i] == target[i]:
                    matchedIdx.add(i)

        for t in triplets:
            if missMatch(t):
                continue
            matchCheck(t)
        
        return len(matchedIdx) == len(target)