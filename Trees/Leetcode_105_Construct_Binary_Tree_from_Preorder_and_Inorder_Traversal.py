'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
'''
'''
Solution:
The trick for this problem is the recognize the list format of both preorder and inorder
for example:
preorder => [3,9,20,15,7] => the first ele from pre is always the root node
inorder  => [9,3,15,20,7] => anything on the left of the root belongs to the left subtree and anything
                             on the right will belong to the right subtree

our goal is to seperate the list and feed them in a recursive function
for example left will be [1: mid+1] on pre since position 0 is the root and it as already been
accounted for. The mid +1 at the end is because python does not count the last ele when splitting the list
If the +1 is not there mid will not be accounted for.
in this example the list that will be pass in are pre = [9] and inorder = [9,3]
the next iteration will just be [] since [1:1] or [0:0] will just give [] as a result

write a base case when it reached the end of the iteration ex: when either pre or inorder are empty
we just return None

apply to same logic on the right side of the list and that is the entire algo.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        # The time complexity would O(N) as we traverse through every nodes
        # Space complexity would be O(D) as D is the depth of the tree as we will 
        # allocate memory on the call stack
    
        def recursiveHelper(preOrder, inOrder):
            if not preOrder or not inOrder: 
                return None
            
            currNode = TreeNode(preOrder[0])
            mid = inOrder.index(preOrder[0])
            currNode.left = recursiveHelper(preOrder[1:mid + 1], inOrder[:mid+1])
            currNode.right = recursiveHelper(preOrder[mid + 1:], inOrder[mid + 1:])
            return currNode
        return recursiveHelper(preorder, inorder)