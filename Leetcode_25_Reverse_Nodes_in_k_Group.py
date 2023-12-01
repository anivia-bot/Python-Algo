# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Time complexity would O(N) and O(1) space
        dummy = ListNode(0, head)
        groupPrev = dummy
    

        def getKth(k, current):
            while current and k > 0:
                current = current.next
                k -= 1
            return current

        while True:
            kth = getKth(k, groupPrev)
            print(kth)
            if not kth:
                break
            
            groupNext = kth.next
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
    


