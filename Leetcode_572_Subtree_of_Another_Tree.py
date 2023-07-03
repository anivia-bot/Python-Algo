# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity would be O(p*q) and O(log(p)) or O(H) space
class Solution:

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        statusLeft = self.sameTree(p.left, q.left)
        statusRight = self.sameTree(p.right, q.right)
        return statusLeft and statusRight



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        status = self.sameTree(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return status or left or right  