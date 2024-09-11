'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X 
there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.
Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''
'''
Solution:

Pass the currMax into the dfs and return the added value so far.
The trick is the perform a DFS and pass 
the currMax value into the dfs function.
create a global variable to track if the counts
of a good nodes.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):
        # Time complexity would be O(N) and space complexity would be O(log(n)) or O(h)

        self.count = 0
        def dfs(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                self.count += 1
                currMax = node.val
            dfs(node.left, currMax)
            dfs(node.right, currMax)

        dfs(root, float('-inf'))

        return self.count