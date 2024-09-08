'''
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

'''
Solution:
There are two ways to solve this problem.

Be creative and think of it as a fixed sliding window problem. l and r ptr will be the same distance n.
when r ptr goes out of bounce then we know the l.next ptr will be the node we want to remove.
The reason l won't be at the nth node is because it will be much easier to do left.next = left.next.next


Fast:
First set a left node (none) and a right node (head)
write a while loop to seperate the two node by n
Once they are both seperated, move both left node and right node to the right until
right node reaches the end of the linked list (out of bounce).
When it is out of bounce we know the left.next node will be exactly at the n position
Set left.next to left.next.next to complete the algorithm.

Slow:
Set 3 ptrs, pre curr and currNext
Reverse the linked list and iterate through the linked list untill it finds 
the n th node. Reverse the linked list back.

Both algo takes O(N) time and O(1) space but the second method is slightly slower as 
we need to travese through the linked list 3 times at max.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):

        # Time complexity would be O(N) and Space Complexity would be O(1)
        dummy = ListNode(0, next=head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next