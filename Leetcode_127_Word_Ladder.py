class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
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