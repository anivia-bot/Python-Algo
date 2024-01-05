'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
'''

'''
Solution:
perform an dfs inorder traversal (operation are in the middle) 
first -> inOrder(node.left) / second -> whatever operations in between / thrid -> inOrder(node.right)
when count == k then return ans.
'''
# O(N) run time and O(h) on the call stack
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        
        self.count = 0
        self.ans = 0
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.val
            inOrder(node.right)
        
        inOrder(root)
        return self.ans
                