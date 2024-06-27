# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root):
        # O(N) time and O(N) space on the call stack.
        def dfs(node):
            if not node:
                return [0,0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            withRoot = node.val + left[1] + right[1]
            withOutRoot = max(left) + max(right)
            return [withRoot, withOutRoot]
        
        return max(dfs(root))