# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # This algo runs in O(NlogK) time and O(1) space
        if not lists or len(lists) < 1:
            return None
        
        def mergeList(l1, l2):
            
            dummy = ListNode()
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
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(mergeList(l1, l2))
            lists = mergedList
        return lists[0]
    