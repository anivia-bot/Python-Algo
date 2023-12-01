'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

'''
Solution:
The trick is to start an extra list node and let it traverse through the two linked list and compare its value
Use a while loop with the condition while l1 and l2 because we are comparing the two lists
if one of the list ran out of values it will throw an error when comparing with none

Care for edge case when either one of the list hasnt been fully explored. Thats why we use if l1 or l2
to check if they have any more values left
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        
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