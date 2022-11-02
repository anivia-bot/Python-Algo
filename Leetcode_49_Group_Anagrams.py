class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # This algo runs in O(M*N) time and O(M) space
        
        resDict = defaultdict(list)
        res = []
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            resDict[tuple(count)].append(s)
        
        for val in resDict.values():
            res.append(val)
        return res