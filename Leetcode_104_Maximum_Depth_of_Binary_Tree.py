# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
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




