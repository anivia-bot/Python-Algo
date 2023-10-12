"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Time O(N) Space O(N)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldNodes = {None:None}
        curr = head

        while curr:
            oldNodes[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = oldNodes[curr]
            copy.next = oldNodes[curr.next]
            copy.random = oldNodes[curr.random]
            curr = curr.next

        return oldNodes[head]