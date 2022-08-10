# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        This is the tortoise and hare algorithm which runs at O(2N) = O(N)
        Space complexity would be O(1) since we only have 2 pointers 
        """
        if not head:
            return False
        slow = head
        fast = head.next
        
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True