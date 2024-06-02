'''
You are given a string s. We want to partition the string into as many parts as possible 
so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, 
the resultant string should be s.
Return a list of integers representing the size of these parts.
Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Solution:

This is a greedy approach, Since we only want to make a string only appear in one sub-string, 
So whenever we have a string's index that is greater than the end index we currently have, we
update the end idx so It will be included in the greater part of the string.

We store the partition when the current index matches the end index which means all char will
only appear in the current string. We store the size of the string and set the size count back to 0
We keep on updating the i index till we reach the end.

In summary, all we need to do is keep expending the end index till the point where i == end index.
When i == end idx we simply add the value into partition and set the size value back to 0.
'''

class Solution:
    def partitionLabels(self, s):
        #O(N) time and O(1) space
        partition = []
        lastIdx = {}
        for idx, char in enumerate(s):
            if char not in lastIdx:
                lastIdx[char] = idx
            lastIdx[char] = idx

        size = 0
        finalIdx = 0
        i = 0

        while i < len(s):
            size += 1
            if finalIdx < lastIdx[s[i]]:
                finalIdx = lastIdx[s[i]]
    
            if i == finalIdx:
                partition.append(size)
                size = 0
            i += 1
        return partition

