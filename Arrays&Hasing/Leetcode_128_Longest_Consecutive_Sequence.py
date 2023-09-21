'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
'''
Solution:
the trick is to make this a O(n) run time
Since hashmap or set takes O(1) run time it will speed up the algorithms (trick 1)
(trick 2) the other trick is the find the lowest number in the consecutive num list
so we write the if statement as if (num - 1) not in numsSet to make sure num is the
smallest num in the consecutive num list

we then write a while loop to figure out how far the consecutive num can go.
Then we compare it with the longest consecutive num using the max function.
'''

# This algo runs in O(N) time and O(N) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numsSet:
                streak = 1
                while num + streak in numsSet:
                    streak += 1
                longest = max(streak, longest)
        return longest
                
