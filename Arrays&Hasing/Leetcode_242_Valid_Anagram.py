class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # The time complexity for this algo is O(N) + O(M) + O(26) = O(N+M) 
        # since we cant guarantee string s and t have the same length
        # Space complexity would be O(26) = O(1) because the most this wordCount dict would save is 26 English char.
        # It does not grow any bigger as the input increases
        
        wordCount = {}
        
        for char in s:
            if char not in wordCount:
                wordCount[char] = 1
            else:
                wordCount[char] += 1
        
        for char in t:
            if char not in wordCount:
                return False
            else:
                wordCount[char] -= 1
                
        for val in wordCount.values():
            if val != 0:
                return False
        return True