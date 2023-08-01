class Solution:
    def numDecodings(self, s: str) -> int:

        # O(N) time and O(1) space
        if s[0] == "0":
            return 0
    
        twoBack = 1
        oneBack = 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = oneBack
            doubleDigits = int(s[i-1:i+1])
            if doubleDigits >= 10 and doubleDigits <= 26:
                current += twoBack
            twoBack = oneBack
            oneBack = current
        return oneBack
