# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # The time complexity would be O(N) since we will be traversing through every nodes of the tree
        # The space complexity would be O(h), h would be the height of the tree since we are using a recursive method
        # The memory will be adding up into the callstack.
        
        def dfs(node):
            
            if not node:
                return (0, True)
            
            leftVal, leftBalanced = dfs(node.left)
            rightVal, rightBalanced = dfs(node.right)
            
            return (max(leftVal, rightVal)+1, leftBalanced and rightBalanced and abs(leftVal - rightVal) <= 1)
        return dfs(root)[-1]
        