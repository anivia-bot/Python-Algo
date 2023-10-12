# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # The time complexity would be O(n) and the space complexity would be O(log(N)) or O(H) which is the
    # height of the binary tree.    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = root.val
        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            self.res = max(self.res, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return self.res