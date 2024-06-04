'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
Example 1:

Input: s = "()"
Output: true

Solution:
Think of this as a decision tree and we use leftMin and leftMax to calculate all the range of 
possibility with a couple edge cases. First if we encounter a left parenthesis, we increase both
min and max by one, if we encounter a right parenthesis and decrease both min and max by one. Finally, when
we reached a *, this is where the divergence happened. We can either increase by treating we have another
left parenthesis or we assume it can be a right(closing) parenthesis. Thats why the range will expend for
leftMin -= 1 and rightMax += 1. If we ever make leftMax < 0 that means we have too many right parenthesis that
we havent been able to close and will never be able to close thats why we return 0.

If our leftMin is less than 0 we reset it back to 0, becasue we know so far all the string can be matched and
the * can be treat it as a non-existing char. Since (*)( will return true if we dont reset the leftMin back to 0
'''


class Solution:
    def checkValidString(self, s):

        # This algo runs in O(N) time and O(1) space
        
        leftMin = 0
        leftMax = 0

        for char in s:
            if char == '(':
                leftMin += 1
                leftMax += 1
            elif char == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            # The reason why leftMax < 0 we return False immediately is because
            # ))(()) if the string looks like this leftMax will be -2 and we can never
            # recover from it since we first start with ) 
            if leftMax < 0:
                return False
            
            # We set leftMin back to 0 is because if leftMin becomes negative that means
            # We guarentee we can at least find a solution so far and will never need it to be negative
            # for example (*)( this will make leftMin negative -1 and we do a +1 on the last char '(' 
            # This will make leftMin == 0 even though it is not a valid solution. To really wrap your head around
            # is to treat negative as a guareentee that from all the string we visited so far we can make a valid 
            # parenthesis. All we need is to complete the rest of the string and see if its valid.
            if leftMin < 0:
                leftMin = 0
                
        return leftMin == 0