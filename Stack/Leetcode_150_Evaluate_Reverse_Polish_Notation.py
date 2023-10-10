'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

'''
Solution:
Dont overcomplicate the problem. This is a classic stack problem.
Set an operator set. iterate through the tokens list. If the value
is an operator, pop the top two elements from the stack and proceed on the operation.
add the result back to the stack since the final value will be reuse to calculate 
for the next operation.

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # This algo runs in O(N) time and O(N) space
        if not tokens:
            return 0

        stack = []
        operators = ('+', '-', '*', '/')

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                secondNum = stack.pop()
                firstNum = stack.pop()
                if t == '+':
                    val = firstNum + secondNum
                    stack.append(val)
                elif t == '-':
                    val = firstNum - secondNum
                    stack.append(val)
                if t == '*':
                    val = firstNum * secondNum
                    stack.append(val)
                if t == '/':
                    val = int(firstNum / secondNum)
                    stack.append(val)
        return stack[0]
