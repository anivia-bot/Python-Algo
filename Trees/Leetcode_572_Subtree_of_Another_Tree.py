'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with
the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and
all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
'''

'''
Solution:
This algorithms requires a same tree helper function to check if the 
trees are the same

next use a dfs function to iterate through the root node and try to find the same tree.
return left or right since if one side is tree then we know the whole tree will at 
least have a subtree that matches the subRoot.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity would be O(p*q) and O(log(p)) or O(H) space
class Solution:
    def isSubtree(self, root, subRoot) -> bool:

        def sameTree(r, s):
            if (not r and s) or (r and not s):
                return False
            if not r and not s:
                return True
            if (r.val != s.val):
                return False
            leftRS = sameTree(r.left, s.left)
            rightRS = sameTree(r.right, s.right)
            return leftRS and rightRS
        
        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

