'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true
'''
'''
Solution:
This question is to apply dfs on p and q at the same time
The trick is the check each condition when interate throguh
the tree that's it

ex: left.val != right.val
(not p and q) or (p and not q) 

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity would be O(p+q) and space complexity would be O(h) or O(log(p))
class Solution:
    def isSameTree(self, p, q):
        def dfs(p, q):
            
            if (not p and q) or (p and not q):
                return False
            
            if not p and not q:
                return True

            if (p.val != q.val):
                return False

            pqLeft = dfs(p.left, q.left)
            pqRight = dfs(p.right, q.right)
            return pqLeft and pqRight
        
        return dfs(p, q)