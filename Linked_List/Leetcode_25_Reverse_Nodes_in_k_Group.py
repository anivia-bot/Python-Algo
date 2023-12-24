'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''

'''
Solution:
The difficult part of this problem is to keep track of where the ptr should be pointing
First, we create a dummy node that points at the head of the linked list
Second, we write a function to find the kth node by passing in groupPrev node and k
Third, set up groupNext to be kth.next and prev to be kth.next as well
This is important because if we reverse the linked list, the first element will be pointing 
at kth.next eventually
ex: 1 -> 2 -> 3 -> 4    =>  3 -> 2 -> 1 -> 4
                        =>  4 <- 1 <- 2 <- 3
Reverse the linked list then we update the ptr
use a tmp to hold the original previousGroup.next (since we reversed the linked list this will be 
the last element from the linked list ex: 1 or 4)
use previousGroup.next to connect to the kth Node (this is where we connect the two reversed linked list)
ex: 3 -> 2 -> 1 -> 6 -> 5 -> 4 (in this case 6 is kth and 1 was previous.next
now update the previousGroup to be tmp (ex: 4)

write an if statement to make sure we our dummy ptr only points at the first kth node since when we reversed
the linked list the first kth node will always be the head and we dont need to update them anymore.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):

        # Time complexity would O(N) and O(1) space
        
        dummy = ListNode()
        dummy.next = head
        prevGroup = dummy
        # The updated is to make sure it will always point to the first kth node
        updated = False
        while True:
            # First find out where the kth node located
            kthNode = self.findKth(prevGroup, k)
            # if kth node goes out of bounce then we dont need to reverse anything
            if not kthNode:
                break
            
            # the first element from the next group
            groupNext = kthNode.next
            # This needs to be point to the next group as we know 
            # (1 -> 2 -> 3) -> 4 we need to let 1 be point at 4 
            # 4 <- (1 <- 2 <- 3)  => (3 -> 2 -> 1) -> 4 
            prev = kthNode.next
            # Just the first element in the linked list
            curr = prevGroup.next

            # reverse the linked list
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # tmp holds the first element but now is the last element from the kth group
            tmp = prevGroup.next
            # the last element (1) will now be point at the first element (6)
            prevGroup.next = kthNode
            # this will become the last element from the first kth group (1)
            prevGroup = tmp

            # this part is to make sure dummy.next will always point at the beginning of the linked list
            if not updated:
                dummy.next = kthNode
                updated = True
        return dummy.next 

    def findKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
            
        return node
