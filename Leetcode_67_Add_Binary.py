class Solution:
    def addBinary(self, a, b):
        
        # Time complexity would be O(N) as we iterate through the input size
        # Space complexity would be O(N) since we reversed the strings into an array
        
        res = ''
        carry = 0
        aList = a[::-1]
        bList = b[::-1]
        
        for i in range(max(len(aList), len(bList))):
            
            aNum = int(aList[i]) if i < len(aList) else 0
            bNum = int(bList[i]) if i < len(bList) else 0
            total = aNum + bNum + carry
            addOn = (total % 2)
            carry = total // 2
            res = str(addOn) + res

        
        if carry:
            res = "1" + res
            
        return res
            
        