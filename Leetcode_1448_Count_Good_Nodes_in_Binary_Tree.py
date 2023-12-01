# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Time complexity would be O(N) and space complexity would be O(log(n)) or O(h)

        self.count = 0

        def dfs(node, maxVal):
            if not node:
                return
            self.count += 1 if node.val >= maxVal else 0    
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root, root.val)
        return self.count