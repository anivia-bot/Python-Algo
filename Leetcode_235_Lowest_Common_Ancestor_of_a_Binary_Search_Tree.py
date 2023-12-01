# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The time complexity for this algo is O(log(n)) since we are visiting half of the tree every time
        # The space complexity would be O(1) as we are not using any extra memory
        currentNode = root
        
        while currentNode:
            if p.val < currentNode.val and q.val < currentNode.val:
                currentNode = currentNode.left
            elif p.val > currentNode.val and q.val > currentNode.val:
                currentNode = currentNode.right
            else:
                return currentNode
              