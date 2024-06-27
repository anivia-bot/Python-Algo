'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Solution:
The trick for this problem is to reverse both num1 and num2 string and mutiply digits by digits
into res array that was set to [0] * (len(num1)+len(num2)) -> 99*99 gives 4 digits max and 10*10 gives 3 digtis min

Since the string is reversed, just use num1 and num2 and iterate over the arrays and compute their value.
use i + j to keep track of which position we can fill the value in. And i + j + 1 to fill the carry numbers.
Check for num is over 10 AND if num + res[i+j] over 10

Once everything is done, remove all leading 0s and join the array strings and return the answer.

'''


class Solution:
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        
        res = [0] * (len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            for j in range(len(num1)):
                num = int(num2[i]) * int(num1[j]) 
                # compute num and check if it goes over 10
                res[i+j] += num % 10
                res[i+j+1] += num // 10
                # compute num + the value thats already in the res[i+j] array
                if res[i+j] >= 10:
                    # rmber to compute res[i+j+1] += res[i+j] // 10 first since if you compute
                    # res[i+j] = res[i+j] % 10 it will overwirte the original value
                    res[i+j+1] += res[i+j] // 10
                    res[i+j] = res[i+j] % 10

        res = res[::-1]
        ptr = 0
        while res[ptr] == 0:
            ptr += 1
        res = res[ptr:]
        for i in range(len(res)):
            res[i] = str(res[i])

        return ''.join(res)