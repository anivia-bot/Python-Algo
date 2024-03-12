'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security systems 
connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

'''
Solution:
The easiest way will be using bottom-up DP approach.
To better understand these type of problems we need to first
understand what sub problem we are dealing with.
In this case we have two chose, we either rob the house
or we dont rob the house. (we cant rob the house next to each other)
Thats why our base case will be nums[i]+nums[i+2] or nums[i+1]
           (i) (i+1) (i+2)
[2,  7  ,9  ,3  ,1 ]   0
If we use a buttom-up approach we need to iterate in reversed order and
add a 0 at the end so we dont go out of bounce.

Another way you can look at it is what is the max value you can earn from 
a specific index, we carry the max you can get and added to that position
In sum, treat this as a climbing stairs problem. Use a bottom up DP approach
and perform two decision which are i+i+2 and i+1
once we iterate to the first position it means we found the most optimal values.
'''
class Solution:
    def rob(self, nums):
        # O(N) time and O(1) space
        nums.append(0)
        for i in reversed(range(len(nums)-2)):
            nums[i] = max(nums[i] + nums[i+2], nums[i+1])

        return nums[0]  