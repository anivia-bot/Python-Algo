'''
A path in a binary tree is a sequence of nodes where each pair of 
adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
'''

'''
Solution:
First we need to realize that the path does not necessarily need to path through the
root node. Second, we are taking a somewhat bottom up approach. we first use a dfs to find the
deepest node and calculate its value. Thrid we travese through the tree back to the top as we calculate 
two things. 

First, check if we treat the current node as root node and see if the current node can form a max path (including 
both leftMax and rightMax and its own value)
Second, check if we don't treat the current node as root, which means we are trying to
form a path through the current node and we will need to pass on either (leftMax or rightMax + curret node val)
Remember to convert negative left or rightMax to 0 if the values returning are negative.
Perform this operation recursively and we will be able to find the max path.

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # The time complexity would be O(n) and the space complexity would be O(log(N)) or O(H) which is the
    # height of the binary tree.    
    def maxPathSum(self, root):

        self.res = float('-inf')
        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            # if the left or right max values are negative just return 0 instead since we 
            # are not including that path.
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # This is to treat the current node as root node and combinding both left and right max
            self.res = max(self.res, node.val + leftMax + rightMax)
            
            # This is to treat the current node as 'passing node' only pick either left or right side 
            # of the path
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return self.res