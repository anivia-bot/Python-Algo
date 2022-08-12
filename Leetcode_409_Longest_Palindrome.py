class Solution:
    def longestPalindrome(self, s: str) -> int:

        # This algorithem runs in O(N) time as we iterate through the entire string
        # O(1) space as the alphabet is fixed. 26 letters, 52 if you count cap case.
        # O(52) = O(1)
        
        stringDict = {}
        for word in s:
            if word not in stringDict:
                stringDict[word] = 1
            else:
                stringDict[word] += 1
                
        if len(stringDict) == 1:
            return len(s)
        
        evenNumber = 0
        OddNumber = 0
        
        for val in stringDict.values():
            if val > 1:
                if (val % 2) == 0:
                    evenNumber += val
                else:
                    evenNumber += (val-1)
                    OddNumber += 1
            else:
                OddNumber += 1
                    
        if OddNumber > 0:
            evenNumber += 1
        
        return evenNumber