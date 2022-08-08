# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # The time complexity will be O(N+M) since we are iterating through two linked list
        # The space complexity will be O(1) since we only have one node and two pointers
        # Linked list problem, try to create a dummy nodes and do if else statement
        # to check which value has the largest value and link the nodes 
        
        dummy = ListNode(0)
        ptr = dummy
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
            else:
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
        
        if l1:
            while l1:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
        if l2:
            while l2:
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
                
        return dummy.next