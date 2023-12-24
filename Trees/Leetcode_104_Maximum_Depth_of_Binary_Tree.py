'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
'''

'''
Solution:
Remeber to add base case on all recursive call
First use a recursive DFS such as return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
Second use BFS which requires a deque. A while loop that runs on deque a for loop that iterate through
everything that is on the q at that point. pass in node.left and node.right into deque and dont forget to add
level after every iteration.
Thrid method use a DFS to iterate through the problem. Still need a stack and while loop to proceed.
The only different is that you need to check node.left before you check node.right and if node will be 
the base case
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        
        # All three solution runs in O(N) time and O(H) space (call stack)

        # Solution 1 DFS recursive
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Solution 2 BFS
    
        # if not root:
        #     return 0
        
        # level = 0
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1 
        # return level

        # Solution 3 DFS iterative
        if not root:
            return 0

        q = deque([[root, 1]])
        level = 0

        while q:
            node, lv = q.popleft()

            if node:
                level = max(level, lv)
                q.append([node.left, 1 + lv])
                q.append([node.right, 1 + lv])
        return level




