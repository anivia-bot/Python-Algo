'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store 
and retrieve keys in a dataset of strings. There are various applications of this data structure, 
such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie 
(i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted 
string word that has the prefix prefix, and false otherwise.
Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''
'''
Solution:
The trick is the realize that this is a Trie problem
The second part will be creating another class called TrieNode inorder for us to iterate 
and navigate through different nodes. (Create a dictionary in this node so we can 
store future nodes in this dictionary, hence dict inside a dict inside another dict)
remember to create an end words and set it to False
Create a root variable at the init function. When performing all operations remember set 
curr = self.root and just use a for loop to iterate through the words and check 
the dictionary status 

'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

# O(N) time and space for all operations

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)