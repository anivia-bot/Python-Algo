class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # O(N) time and O(1) space
        
        carry = 0
        newSum = digits[-1] + 1
        if newSum == 10:
            carry += 1
        else:
            digits[-1] += 1
            return digits
        
        for i in reversed(range(len(digits))):
            if carry > 0:
                newSum = digits[i] + 1

                if newSum == 10:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] = newSum
                    carry = 0
        if carry:
            return [carry] + digits
        return digits
