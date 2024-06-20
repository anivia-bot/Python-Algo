# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         # O(logn) time and O(log(n)) space

#         def helper(x, n):
#             if x == 0:
#                 return 0
#             if n == 0:
#                 return 1
            
#             res = helper(x, n//2)
#             res = res * res
#             return x * res if n % 2 else res

#         res = helper(x, abs(n))
#         return res if n >= 0 else 1/res

'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Solution:
The trick for this problem is to use recursion to and divide the n value in half
to achieve to log(n) time and space complexity. 

Remember to use abs value before passing into the helper function as we will handle the negative
value at the final return statement.

We basically keep dividing n // 2 till n reaches n == 0 and start move all the way up with the results.
When dividing odd n values remember to x * res before returning. Why ? here's a demonstration.

                                2^50
                                /
                            2^25*2^25
                            /
                        2*(2^12*2^12) (Since the previous value is odd we will need to add one more 2 into it)
                        /                (So whenever there's a odd number, multiply another 2 with it)
                    2^6*2^6
                    /
                2*(2^3*2^3) 
            

'''

# time complexity O(log(n)) space complexity O(log(n))
class Solution:
    def myPow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        def helper(x, n):
            if n == 0:
                return 1
            res = helper(x, n//2)
            res = res * res
            return x * res if n % 2 != 0 else res
        
        ans = helper(x, abs(n))
        return ans if n > 0 else 1/ans