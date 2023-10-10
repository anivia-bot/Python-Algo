'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''
'''
Solution:
This is a classic backtracking problem.
For all backtracking you need to set base case for your decision tree to stop
The basecase for this will be both the left count and right count reaches n.
join the string from tmp and append it into res

generate the decison tree. left + 1 and right + 1
(one condition for the right to + 1 is that the left > right so we have a valid parentheses) 
since this is a backtracking problem, we will need to pop the val before we continue the decision tree

steps: 

set a function, set a basecase for the decision tree to stop, 
generate parenthesis for both left and right, 
set basecases for both backtracking path. 
pop the result since we are doing backtracking and we cant reuse the
result so we will need tp pop the value

'''



class Solution:
    def generateParenthesis(self, n):

        # The time complexity would be Catalan numbers which is O((4^n)/sqrt(n))) 
        # The space complexity would be O(N) as it was the depth of the tree which is 2N = O(N)
        # The result does not count as our space complexity if you count the answer it will be O((4^n)/n*sqrt(n))) 
        tmp = []
        res = []

        def backtracking(left, right):
            if left == n and right == n:
                tmpString = ''.join(tmp)
                res.append(tmpString)
                return
            
            if left < n:
                tmp.append('(')
                backtracking(left + 1, right)
                tmp.pop()
            
            if right < left:
                tmp.append(')')
                backtracking(left, right + 1)
                tmp.pop()

        backtracking(0,0)
        print(len(res))

        return res