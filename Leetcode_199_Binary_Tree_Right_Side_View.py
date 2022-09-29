# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Time complexity would be O(N) as we will traverse the entire tree using BFS
        # Space complexity would be O(N) since we are using a q data structure. The worst case would be O(N)
        
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            
            rightSideNode = None
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                
                if node:
                    rightSideNode = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSideNode:
                res.append(rightSideNode.val)
                
        return res
                