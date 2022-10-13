# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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