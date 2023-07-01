# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # The time complexity would be O(N) and the space complexity would be O(N) for the worst case
        # O(H) height of the tree for the average case and O(logN) if the tree is balanced
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.diameter