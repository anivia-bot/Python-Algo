# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        dq = collections.deque()
        curr = head

        while curr:
            dq.append(curr)
            curr = curr.next
        while dq:
            left = dq.popleft()
            head.next = left
            head = head.next
            if dq:
                right = dq.pop()
                head.next = right
                head = head.next
            if not dq:
                head.next = None
        return curr 
                
