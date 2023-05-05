class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Middle out algo will take O(N^2) time complexity
        # The first N time complexity would be iterate through the entire string, the N time 
        # complexity would be checking if the current string is a palindrom
        # O(1) space complexity
        
        self.res = ''
        self.resLen = 0
        
        def checkPalindrom(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currentStringL = r - l + 1
                if currentStringL > self.resLen:
                    self.res = s[l:r+1]
                    self.resLen = currentStringL
                l -= 1
                r += 1
        
        for i in range(len(s)):
            
            # odd string cases
            l, r = i, i
            checkPalindrom(l, r)
                        
            # even string cases
            l, r = i, i + 1
            checkPalindrom(l, r)
            
        return self.res
            