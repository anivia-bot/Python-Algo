'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
'''
'''
Solution:
The diameter is essential the longest on the left side and the longest on the right side
use dfs on both left and right and add them together will give the answer
check max diameter on every dfs iteration and dont forget to write base case and 
1 + max(left, right) when returning values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        
        # The time complexity would be O(N) and the space complexity would be O(N) for the worst case
        # O(H) height of the tree for the average case and O(logN) if the tree is balanced
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.diameter