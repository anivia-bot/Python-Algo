class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Since we are iterating through the entire input. We are expecting a O(N) solution
        # We have an extra dictionary however this dictionary will not grow as our input 
        # and since there are only 26 letters in the alphabets so the Space complexity would be constant which is 
        # O(1) !

        magWords = {}
        for word in ransomNote:
            if word not in magWords:
                magWords[word] = 1
            else:
                magWords[word] += 1
        
        for word in magazine:
            if word in magWords and magWords[word] != 0:
                magWords[word] -= 1
                
        for val in magWords.values():
            if val != 0:
                return False
            
        return True
                
        