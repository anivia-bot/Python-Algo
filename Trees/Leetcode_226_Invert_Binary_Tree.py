'''
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
'''
'''
Solution:
Start with base case that when not root we return None
set a tmp variable to hold root.left
swap root.left with root.right and root.right with tmp
use a recursive call on the root.left and root.right 
return rootS

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
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