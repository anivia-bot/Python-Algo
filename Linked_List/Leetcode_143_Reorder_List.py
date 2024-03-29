'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
'''
'''
Solution:
This problem requires multiple tricks:

First we need to seperate the linked lists in half

Second we need to reverse the second half of the linked list by applying slow and fast ptr
remember to apply while fast and fast.next since it will go out of bounce and we need to take 
care of the edge case. Also slow will be at the starting position (head) and fast will be (head.next)

Third we need to reverse the second half of the linked list. Rmbr currNext need to be inside the while loop 
and prev will be what we return since curr will be at the out of bounce position

Fourth set two variable and merge the two linked list together. The second part of the linked list
is always smaller so we can just write while second and wait for the loop to break.
use tmp1 and tmp2 to track the next position, then merge the two linked list.
'''
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2        