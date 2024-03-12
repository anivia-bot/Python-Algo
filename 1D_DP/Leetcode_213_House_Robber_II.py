'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police 
if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''

'''
Solution:

House robber II is a very similar problem just like house robber.
You can use a bottom-up dynamic programming to tackle this problem.
The only differences are the value you passed in. Since the neighborhood is in
a circle, all we need to care about is not including the last house if you rob the first house (since it is in
a circle neighborhood the last house will be adjcent to the first house) vice versa
and if you skip the first house and rob the second house the last house will be adjcent to the first house


'''

class Solution:
    def rob(self, nums):
        # Time is O(N) and space is O(1)
        # if there are only one number in nums
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            nums.append(0)
            # Since we are doing len(nums)-2, any array with a len less or equal than 2 will be ignored.
            # Hence, if the array is [1] we then append it with nums.append(0) we will now have
            # an array of size 2 which the for loop may not execute, thats why we need a condition of
            # if len(nums) == 1 we simple return the result. We need at least 2 element inorder for us
            # to start robbing houses, (since we will be appending 0 which makes the array size to be 3)
            for i in reversed(range(len(nums)-2)):
                nums[i] = max(nums[i] + nums[i+2], nums[i+1])
            return nums[0]
        if not nums:
            return 0
        
        withoutFirstRob = helper(nums[1:])
        withFirstRob = helper(nums[:-1])
        return max(withoutFirstRob, withFirstRob)