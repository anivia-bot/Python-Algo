# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Time complexity would be O(N) as it traverse through the entire tree
        # Space complexity would be O(N) as well as we counted the call stack on recursion
        
        self.ans = None
        def dfs(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            
            l = dfs(root.left,p,q)
            r = dfs(root.right,p,q)
            
            if l and r:
                return root
            elif l or r:
                return l or r
            
        self.ans = dfs(root,p,q)
        return self.ans