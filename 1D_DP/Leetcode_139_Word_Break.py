'''
Given a string s and a dictionary of strings wordDict, return true 
if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
'''
Solution:
This is another classic DP backtracking approach. Essentially, we set a base case to be
True at the end of the dp array. Then we iterate over the index of the string AND every
word in the dictionary. If the current idx + the len of the word is > than the len of the string
we know the result would be out of bounce and will not be consider. If we find a perfect match,
we use dp[i] = dp[i+len(w)], if dp[i] is True than we can break out of the wordDict loop.
Let me further explain the logic behind this, Let's say if we find a match of the string from
the wordDict however, dp[i+len(w)] might be false, for example wordDict = ["leet", "code] with the
word "leetcodeoo"  -> when we are at 4th index, we found out that code would be a match but the remaining
"oo" after "code" still remain unmatch, thus dp[4] would still remain False. 

'''
# Two different dp approach
# Both run in O((N^2)*M) time and take O(N) space
class Solution:
    def wordBreak(self, s, wordDict):
        
        dp = [True] + [False]* len(s)
        
        for idx in range(1, len(s)+1):
            for word in wordDict:
                if dp[idx-len(word)] and s[idx-len(word):idx] == word:
                    dp[idx] = True
                    
        return dp[-1]
                
                
                        
class Solution:
    def wordBreak(self, s, wordDict):
        
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]