'''
Given the root of a binary tree, 
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''

'''
Solution:
Apply a simple BFS to solve this problem
use a couple if statement so filter out null node
tmp will be adding the current node

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        
        # The time complexity for this algo would be O(N) as we traverse through the enitre tree once
        # The space complexity would be O(N/2) = O(N) as we on average would be storing all the nodes
        # into the queue

        if not root:
            return []   
        ans = []
        q = deque()
        q.append(root)

        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp.append(node.val)
            ans.append(tmp)
        return ans



            
            