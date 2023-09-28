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
        
        parentheseDict = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        queue = []
        
        for char in s:
            if char in parentheseDict:
                if not queue:
                    return False
                else:
                    queueElement = queue.pop()
                    if parentheseDict[char] != queueElement:
                        return False
            else:
                queue.append(char)
            
        if len(queue) == 0:
            return True
        else:
            return False
            