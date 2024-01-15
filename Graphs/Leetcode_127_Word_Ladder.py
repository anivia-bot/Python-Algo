'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

'''
'''
Solution:
The goal is to break it down to a BFS problem
We first need to create an adjList with all the pattern with words included.
ex:{ *og: [dog, log, cog] }
Once we created the adj list we add the beginWord into visited an q and start our path
at 1 since begin word is also counted as 1 path.

Now peform a BFS search, if any word == endWord then we return path else
we iterate over each patterns and add it to q and visited. increment path 
after each full iteration from the for loop.
If everything has been processed and no return then we return 0
'''


from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        # This algo runs in O((N^2)*M)
        # The space complexity would be O(N*M)
        
        if endWord not in wordList:
            return 0
        
        nei = {}
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                if pattern not in nei:
                    nei[pattern] = []
                nei[pattern].append(word)
                
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)
        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiPattern in nei[pattern]:
                        if neiPattern in visited:
                            continue
                        else:
                            visited.add(neiPattern)
                            q.append(neiPattern)
            res += 1
        return 0