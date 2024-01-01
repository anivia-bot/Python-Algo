'''
Serialization is the process of converting a data structure or object into a sequence of bits so 
that it can be stored in a file or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be 
serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

'''
'''
Solution:
There are many ways you can implement this algo.
But today we will decusee the dfs way
We first implement a preorder traversal as it will follow the same step of a DFS algo when 
we deserealize the tree.
Store the tree into a list including the Null node and convert it into a string
(that's it for seralizing)

covert the searlize string back to a list and use a global variable count to 
track where the string will navigate throughout the dfs traversal
apply dfs and preorder traversal to achieve the tree traversal.
Ex: create curret Node then node.left = dfs() then node.right = dfs()


'''
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Three different approaches have been provided for this problem
# 2 DFS solution and 1 BFS solution which all runs in O(N) time and space complexity

# This is the BFS soultion 
class Codec:
    
    def serialize(self, root):
        
        if not root:
            return ''
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            node = q.popleft()
            if not node:
                res.append('None')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        resString = ','.join(res)
        return resString


    def deserialize(self, data):
        if not data:
            return None
        
        dataList = data.split(',')
        count = 0
        q = deque()
        root = TreeNode(int(dataList[0]))
        q.append(root)
        
        while q:
            node = q.popleft()
            count += 1
            if count < len(dataList) and dataList[count] != 'None':
                node.left = TreeNode(int(dataList[count]))
                q.append(node.left)
            count += 1
            if count < len(dataList) and dataList[count] != 'None':
                node.right = TreeNode(int(dataList[count]))
                q.append(node.right)
        return root


# This is the DFS solution
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []
        def dfs(node):
            if not node:
                res.append('None')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
            
        dfs(root)
        resString = ','.join(res)
        return resString
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        vals = data.split(',')
        self.count = 0
        
        def dfs():
            if vals[self.count] == 'None':
                self.count += 1
                return None
            
            node = TreeNode(int(vals[self.count]))
            self.count += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


# This is another DFS approach
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []
        def dfs(node):
            if not node:
                res.append('None')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
            
        dfs(root)
        resString = ','.join(res)
        return resString
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        vals = data.split(',')
        self.count = 0
        
        def dfs(node):
            if not node:
                self.count += 1
                return None
            root = TreeNode(int(vals[self.count]))
            self.count += 1
            root.left = dfs(TreeNode(int(vals[self.count]))) if vals[self.count] != 'None' else dfs(None)
            root.right = dfs(TreeNode(int(vals[self.count]))) if vals[self.count] != 'None' else dfs(None)
            return root
        return dfs(TreeNode(int(vals[self.count]))) if vals[self.count] != 'None' else dfs(None)

        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))