
# Two different dp approach
# Both run in O((N^2)*M) time and take O(N) space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [True] + [False]* len(s)
        
        for idx in range(1, len(s)+1):
            for word in wordDict:
                if dp[idx-len(word)] and s[idx-len(word):idx] == word:
                    dp[idx] = True
                    
        return dp[-1]
                
                
                        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]* (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            if dp[i] is True:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i + len(word)] = True
        return dp[-1]