# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time complexity would be O(N) as we iterate through the entire linked list
        # Space complexity would be O(1)
        
        if not head:
            return
        
        prevNode = None
        currNode = head
        
        while currNode:
            currNext = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = currNext
        return prevNode