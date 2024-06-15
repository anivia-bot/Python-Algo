'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a 
cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1



Solution: 
Since we are guarantee a solution, we can simply iterate the loop as many time as we want by 
setting if n not in seen. If we found a num that we computed that means there's a loop and 
we will never find a happy number. If the result is == 1 then we simply return True.

'''


class Solution:
    def isHappy(self, n: int) -> bool:
        # O(n) time and O(n) space
        seen = set()

        while n not in seen:
            seen.add(n)
            tmp = 0
            for i in str(n):
                tmp += (int(i))**2
            if tmp == 1:
                return True
            n = tmp

        return False
