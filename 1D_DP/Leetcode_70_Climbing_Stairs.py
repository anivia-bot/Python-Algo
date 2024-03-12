'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top
 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
'''
Solution:
The true bottom up DP approach takes we just need to use two variable to keep track
of how many stairs to climb

We have n numbers but we only run operations n - 1 times
since we are starting from both 4 and 5 (one, two)
After we compute stair 1 and 2 we know the total staris 
we are not calculating (combining) stair 1 and 0.

ex:
0     1     2      3      4     5
8    (5    (3)    (2)    (1)    1)
In sum we set our base case to be both 1 at 5 the default is 1 and at 4 you can only take 1 step
We iterate n - 1 time (since we might go out of bounce) 
we then return one

if we can take three steps then the inital val will be 1, 1, 2 since at step 3 we can take either
1 or 2 ways to move forward. 

'''
class Solution:
    def climbStairs(self, n):
        
        # This is a Dynamic Programming solution with O(N) time complexity as we only iterate through
        # the input once.
        # O(1) space complexity as we only used two variables
        
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
        