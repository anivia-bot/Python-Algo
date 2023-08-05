class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Time and Space are both O(N*M)
        
        dp = [[float('inf')] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dp[-1][i] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[j][-1] = len(word2) - j
        print(dp)
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[j][i] = dp[j + 1][i + 1]
                else:
                    dp[j][i] = 1 + min(dp[j + 1][i + 1], dp[j][i + 1], dp[j + 1][i])
        return dp[0][0]