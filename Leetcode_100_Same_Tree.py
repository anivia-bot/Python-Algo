# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity would be O(p+q) and space complexity would be O(h) or O(log(p))
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        statusLeft = self.isSameTree(p.left, q.left)
        statusRight = self.isSameTree(p.right, q.right)

        return statusLeft and statusRight