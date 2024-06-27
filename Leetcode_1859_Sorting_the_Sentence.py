class Solution:
    def sortSentence(self, s):
        wordDict = {}
        cnt = 0
        tmpS = ''
        res = ''
        i = 0

        while i < len(s):
            if s[i].isalpha():
                tmpS += s[i]
                i += 1
            elif s[i].isnumeric():
                numCnt = 0
                num = s[i]
                # Just in case the number exceeded 10 in the actual coding interview
                while i+1 < len(s) and s[i+1].isnumeric():
                    num += s[i+1]
                    i += 1
                wordDict[int(num)] = tmpS
                tmpS = ''
                cnt += 1
                i += 1
            else:
                i += 1
                continue

        for j in range(1,cnt+1):
            if j == 1:
                res = wordDict[j]
                continue
            res = res + ' ' + wordDict[j]
        return res

