'''
Given the root of a binary tree, 
imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
'''

'''
Solution:
The trick for this problem is the realize
we can just pick the last element from the BFS algorithms
and it will always be the right side view.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root):

        # Time complexity would be O(N) as we will traverse the entire tree using BFS
        # Space complexity would be O(N) since we are using a q data structure. The worst case would be O(N)

        if not root:
            return []
        
        ans = []
        q = deque()
        q.append(root)

        while q:
            tmp = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if (i + 1) == tmp:
                    ans.append(node.val)
        return ans
                