class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time O(N^2) and O(1) space
        self.res = 0

        def checkP(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            checkP(i, i)
            checkP(i, i + 1)

        return self.res
