'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

'''
Solution:
First you need to set a carry variable and head and dummy node
Then you iterate through l1 and l2 until one of the linked list reaches the end
compute the sum of two linked list node and use the % to keep the unit digits 
if there is carry assign it with the total sum

care for edge cases such as l1 or l2 has different length. We need to make sure to run
while loop on both linked list to ensure they both reaches the end
check for the last edge case where carry hasnt been assign when both linked list reaches the end
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        carry = 0
        head = ListNode(0)
        dummy = head

        while l1 and l2:
            total = (l1.val + l2.val + carry) % 10
            head.next = ListNode(total)
            head = head.next
            carry = (l1.val + l2.val + carry)//10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = (l1.val + carry) % 10
            head.next = ListNode(total)
            head = head.next
            carry = (l1.val + carry)//10
            l1 = l1.next

        while l2:
            total = (l2.val + carry) % 10
            head.next = ListNode(total)
            head = head.next
            carry = (l2.val + carry)//10
            l2 = l2.next

        if carry > 0:
            head.next = ListNode(carry)
            head = head.next

        return dummy.next


        