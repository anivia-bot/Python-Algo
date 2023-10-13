'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

'''
Solution:

basically you need to have 3 ptr to perform a reverse operation
A prev, curr and nxt ptr, nxt ptr should be created inside the while loop as it will go out of bounce
if you define it prior to the loop

remember to return prev in the end as current will eventually go out of bounce (breaking the while loop)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
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