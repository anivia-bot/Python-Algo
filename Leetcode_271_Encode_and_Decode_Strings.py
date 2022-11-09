class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # The time and space complexity of this algo runs in O(N) and take O(N) space
    def encode(self, strs):
        res = ''
        for s in strs:
            sLen = str(len(s))
            sAdd = sLen+'#'+s
            res += sAdd
        return res
            

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        res = []
        i = 0

        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            num = int(strs[i:j])
            s = strs[j+1: j+1+num]
            res.append(s)
            i = j+1+num
        return res
