class TrieNode:

    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:
    # O(N) time since it is a-z O(26N) = O(N)
    # O(N) space

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.child.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
            return curr.end
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


