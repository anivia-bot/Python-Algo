class Solution:
    def findAnagrams(self, s, p):
        
        # This run in O(N) time since we only iterate through the s string once
        # The space complexity would be O(1) as the sHash and pHash will only hold up to 26 alphabets
        
        if len(p) > len(s):
            return []
        
        sHash, pHash = {}, {}
        res = []
        
        for i in p:
            if i not in pHash:
                pHash[i] = 1
            else:
                pHash[i] += 1
        
        for j in range(len(p)):
            if s[j] not in sHash:
                sHash[s[j]] = 1
            else:
                sHash[s[j]] += 1
        
        if sHash == pHash:
            res.append(0)
        
        l = 0
        
        for r in range(len(p), len(s)):
            
            if s[r] not in sHash:
                sHash[s[r]] = 1
            else:
                sHash[s[r]] += 1
            
            sHash[s[l]] -= 1
            
            if sHash[s[l]] == 0:
                sHash.pop(s[l])
            l += 1
            if sHash == pHash:
                res.append(l)
        return res