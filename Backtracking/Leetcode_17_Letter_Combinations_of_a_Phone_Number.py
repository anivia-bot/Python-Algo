'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''
'''
Solution:
This is another classic backtracking problem.
We first create a dict with all the numbers map to its letter
Then we iterate through every combination with a for loop and
backtracking, set base case to capture when curr can we added to 
the res.
'''


class Solution:
    def letterCombinations(self, digits):
        
        # Time complexity would be O(N*(4^N)) as we use the backtracking approach
        # Space complexity would be O(N*(4^N)) as well
        
        if not digits:
            return []

        digitsMap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r', 's'],
            '8':['t','u','v'],
            '9':['w','x','y', 'z']
        }
        res = []
        def backtracking(i, curr):
            if len(curr) == len(digits):
                tmp = curr.copy()
                ans = ''.join(tmp)
                res.append(ans) 
                return
            if i >= len(digits):
                return
            
            for j in range(len(digitsMap[digits[i]])): #(0,1,2)
                char = digitsMap[digits[i]][j]
                curr.append(char)
                backtracking(i+1, curr)
                curr.pop()

        backtracking(0, [])
        return res