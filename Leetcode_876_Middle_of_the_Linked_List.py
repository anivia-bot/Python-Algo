# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        
        # O(N) Time complexity and O(1) space
        self.count = 0
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.count = max(self.count, left + right)
            return max(left, right) + 1
        dfs(root)   
        return self.count