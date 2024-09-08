'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of 
the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''

'''
Solution:

Watch out when head or head.next does not exist ex: [] or [1]
Write condition before we start fast = head.next or else we will be none has not method .next
The trick is the have a fast ptr and a slow ptr

the fast ptr will be head.next and the slow ptr will be head
run while loop on slow ptr because if there is NOT a loop then it will 
eventually be detected with the if statement

remember to use if not fast or fast.next to check if fast is still a linked list node
or else it will rasie and error saying none type object has not attribute 

lastly if fast == slow then we found the loop 
else we just update the ptr
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        This is the tortoise and hare algorithm which runs at O(2N) = O(N)
        Space complexity would be O(1) since we only have 2 pointers 
        """
        if not head:
            return False

        fast = head.next
        slow = head
        while slow:
            if not fast or not fast.next:
                return False
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False