'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
 
Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''
'''
Solution:
First we need to create a TrieNode class with dict and end value defalut as False
The main part will be the search function, we will need to iterate all combination when
the word is '.' (set another for loop for curr.child.values) since we will be repeating 
all of the operations again and again we use a recursive call with i + 1 (since it will be
the word after '.' and we pass in k as the next next node)
'''

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


