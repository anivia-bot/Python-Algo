# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # The time complexity for this algo would be O(N) as we traverse through the enitre tree once
        # The space complexity would be O(N/2) = O(N) as we on average would be storing all the nodes
        # into the queue
        q = deque()
        q.append(root)
        res = []
        
        while q:
            lenQ = len(q)
            levelRes = []
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    levelRes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levelRes:
                res.append(levelRes)    
        return res
                
            
            
            
            