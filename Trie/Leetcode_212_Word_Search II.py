'''
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''

'''
Solution:
The reason we need to apply Trie is because we need to utalize hashmap look up time
It is for the time complexity of the algoritms

First create a TrieNode class with dict and end as its parameter
Create an add words function so we can add TrieNode into the Trie
Iterate through the words and add every words into the Trie
The root node should look like this 
{
    root: {nodeA:{nodeD....}, 
            nodeB:{node G, ...}, 
            nodeC}
}
create a visited and res set so we can properly run our dfs
create a dfs function and its base case: row and col in bound,
(r, c) not in visited, board[r][c] in node.child

after all the based case has passed. add the current corrdinate (r, c) to visited
update word by using +=, update curr node to curr.child
if the current node.end is True then add it to res
perform dfs on 4 direction, and remove visited after all dfs has been ran.

use a for loop to iterate through the entire matrix and pass in r and c
'''

# Time complexity would be O(m*n*4^w) 
# (w is the average word len, 4 is because dfs goes in 4 direction, m*n would be the dimention of the grid) 
# Space complexity would be O(w) + O(size of the trie) -> best case would be all char be the same
# worst case would be all char are unique which is O(N) hence -> O(W) from the depth of the call stack  
# O(W + N)
class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Solution:
    def addWords(self, node, word):
        curr = node
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.end = True
        return

    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            self.addWords(root, word)

        rLen = len(board)
        cLen = len(board[0])
        # The reason we use set for res is beacuse set is immutable
        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if ((r < 0) or (r >= rLen) or (c < 0) or (c >= cLen) or ((r, c) in visited) or
                board[r][c] not in node.child):
                return
            visited.add((r, c))
            word += board[r][c]
            node = node.child[board[r][c]]
            if node.end:
                res.add(word)
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visited.remove((r, c))

        for r in range(rLen):
            for c in range(cLen):
                dfs(r, c, root, '')
        return list(res)
