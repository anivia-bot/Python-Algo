class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(N) time and O(N) space
        dp = [0] * (n + 1)
        powerTrack = 1

        for i in range(1, n + 1):
            if powerTrack * 2 == i:
                powerTrack = i
            dp[i] = 1 + dp[i - powerTrack]
        return dp