class Solution:
    def calculate(self, s):
        # Time complexity would be O(N)
        # Speace complexity would be O(N) as well
        cur = 0 
        res = 0
        sign = 1
        stack = []
        
        
        for char in s:
            if char.isdigit():
                cur = cur*10 + int(char)
            elif char in ['+', '-']:
                res += sign*cur
                sign = 1 if char =='+' else -1
                cur = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            
            elif char == ')':
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign * cur