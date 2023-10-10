'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which this is possible, 
keep answer[i] == 0 instead.
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 
'''
'''
Solution:
This is quite a tricky problem to be implementing stack 
Need to be thinking in a way that you move forward with 
your index and start popping once you find larger tmp.
!! Stack will only be stacking up when temperature is decreasing !!
(or else it will be pop and added back to the result)

define a list of 0s for res (since if we find no warmer days we will be 
returning 0s anyway)
tmp will be our stack

use a for loop to iterate through the temperatures array
use a while loop to pop the stack and check insert the index
when adding tmp to the stack remeber to add its index so it will 
be easier to insert to the right pos in res.

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # O(N) time and space
        res = [0] * len(temperatures)
        tmp = []

        for idx, val in enumerate(temperatures):
            while tmp and tmp[-1][1] < val:
                res[tmp[-1][0]] = (idx - tmp[-1][0])
                tmp.pop()
            tmp.append([idx, val])
        return res