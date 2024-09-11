'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
'''
'''
Solution:

Split occur is where the lowest common ancestor is.
The trick to understand lowest common ancestor is the understand
that when a split occur, that is where the LCA is.
for example. p < LCA and q > LCA. we know that p is smaller than the current node 
and q is greater than the current node. That must mean that the current node
is the LCA

the else statement basically says:
LCA can also be a node of p or q, so p, q is either both smaller/greater than LCA
or else the current node is either equals p or q or it is at where the split occur.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
              