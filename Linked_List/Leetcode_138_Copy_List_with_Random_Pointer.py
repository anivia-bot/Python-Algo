'''
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to 
new nodes in the copied list such that the pointers in the original list and 
copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, 
or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''

'''
Solution:

Create a dict that store all the newly created node mapping to the old node.
{
    oldNode : newNode
}

This newNode does not contain next nor random.  That's why we need another while loop
to map the random and next for all the new Node.


The trick is to run a while loop twice
the first loop creates a copy of all nodes and save it into a dict
create a copy node then run the next while loop
the second loop use the old linkedlist node as a key to point to the value to the copy node
linked the random node move both curr node and copy node to the next node
return the dummy node 
'''

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Time O(N) Space O(N)
class Solution:
    def copyRandomList(self, head):

        oldToNew = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr =  curr.next   
        
        copyCurr = oldToNew[head]
        dummy = copyCurr
        oldCurr = head
        while oldCurr:
            copyCurr.next = oldToNew[oldCurr.next]
            copyCurr.random = oldToNew[oldCurr.random]
            copyCurr = copyCurr.next
            oldCurr = oldCurr.next
        return dummy 
        
