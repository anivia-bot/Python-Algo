# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Time complexity would be O(N) since each nodes will only be visited once
        # Space complexity would be O(h). h as in the height of the tree because if we call the
        # Tree in a recursive way, it will take up memories in the call stack.
        if not root:
            return 
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root