'''
Given a binary tree, determine if it is 
height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
'''

'''
Soution: 
To determine the height of a binary tree we need to take the 
bottom-up approach and apply dfs to the algorithms

For any dfs approach applying a based case at the begining is crucial.
Our base case for this problem is when node is None, in this case we return (True, and 0) 
as we do not consider null node as height

we check if the tree at the current node is balanced or not we used a variable balanced
to check if the left subtree and the right subtree is balanced 
balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
finally we return the [balanced and 1 + max(left[1], right[1])]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        
        # The time complexity would be O(N) since we will be traversing through every nodes of the tree
        # The space complexity would be O(h), h would be the height of the tree since we are using a recursive method
        # The memory will be adding up into the callstack.
        
        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            # The reason we have 1 + max(left[1], right[1]) is because we are tring to find 
            # the height at each node from bottom to top. Think of it as trying to find out
            # the height of every node and when you return these value it will refeclt on the left or right
            # and if at a certain level the left and right isn't balanced we can simply make balanced false
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
        
        