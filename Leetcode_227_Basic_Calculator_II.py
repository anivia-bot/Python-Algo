class Solution:
    def calculate(self, s: str) -> int:

        # The time complexity for this algorithm would be O(N)
        # The space complexity for this algo would be O(N) as well
        stack = []
        operator = '+'
        curr = 0
        opSet = {'+','-','*','/'}
        numSet = set(str(x) for x in range(10))
        
        
        
        for indx in range(len(s)):
            if s[indx] in numSet:
                curr = curr*10 + int(s[indx])
                
            if s[indx] in opSet or indx == len(s)-1:
                
                if operator == '+':
                    stack.append(curr)
                
                elif operator == '-':
                    stack.append(-curr)
                
                elif operator == '*':
                    stack[-1] *= curr
                    
                elif operator == '/':
                    stack[-1] = int(stack[-1]/curr)
                
                curr = 0
                operator = s[indx]
            
        return sum(stack)