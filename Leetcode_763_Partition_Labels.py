class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #O(N) time and O(1) space
        indexDict = {}
        for idx, val in enumerate(s):
            indexDict[val] = idx

        res = []
        size = 0
        lastIdx = 0

        for idx in range(len(s)):
            size += 1
            lastIdx = max(lastIdx, indexDict[s[idx]])

            if idx == lastIdx:
                res.append(size)
                size = 0
        return res