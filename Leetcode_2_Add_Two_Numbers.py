# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        head = ListNode(0)
        dummy = head

        while l1 and l2:
            total = (l1.val + l2.val + carry) % 10
            head.next = ListNode(total)
            head = head.next
            carry = (l1.val + l2.val + carry)//10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = (l1.val + carry) % 10
            head.next = ListNode(total)
            head = head.next
            carry = (l1.val + carry)//10
            l1 = l1.next

        while l2:
            total = (l2.val + carry) % 10
            head.next = ListNode(total)
            head = head.next
            carry = (l2.val + carry)//10
            l2 = l2.next


        if carry > 0:
            head.next = ListNode(carry)
            head = head.next

        return dummy.next


        