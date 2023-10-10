'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

'''
Solution:
Append opening bracket into the stack. pop the stack when we encounter a closing bracket
compare if the value of the closing bracket equals to the opening bracket

Care for edges cases such as stack is empty and we have a closing bracket (nothing to pop from stack)

'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        # The time complexity is O(N) since we are going over the entire array once
        # Space complexity would be the parentheseDict O(3) + queue O(N) = O(N)
        # The trick is the have a parenthese dict that you can check if it is the correct parenthese
        # Check the queue if it is a closing parenthese
        # Add to queue if it is a opening parenthese
        # Check the queue if is empty or not 
        
        if not s:
            return False
        
        parenthesesDict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
        for char in s:
            if char not in parenthesesDict:
                stack.append(char)
            else:
                if stack:
                    openingBracket = stack.pop()
                    closingBracket = parenthesesDict[char]
                    if openingBracket != closingBracket:
                        return False
                else:
                    return False
        return True if not stack else False

            