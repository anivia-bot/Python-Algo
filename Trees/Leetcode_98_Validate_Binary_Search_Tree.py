'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true
'''

'''
Solution:
The trick for this is to make sure the left and right nodes are in bounds
for example node.left you need to be careful of the right bound (hence cant be bigger than the previous node)
vice versa for node.right 
use a dfs to iterate through the tree.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):

        if not root:
            return True
        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            if node.val <= leftBound or node.val >= rightBound:
                return False
            left = dfs(node.left, leftBound, node.val)
            right = dfs(node.right, node.val, rightBound)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
