class Solution:

    def checkPalindrome(self, s, l, r):
        # Time complexity would be O(N*2^N)
        # Space complexity would be (N^2) one N from the call stack and the other N is from the tmp list
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        tmp = []
        
        def dfs(i):
            if i >= len(s):
                res.append(tmp.copy())
                return
            for j in range(i, len(s)):
                if self.checkPalindrome(s, i, j):
                    tmp.append(s[i:j+1])
                    dfs(j + 1)
                    tmp.pop()
        dfs(0)
        return res