'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
'''
Solution:
The trick of for this problem is to realize that this can be seperated into two different problem
One is merging two linked lists (divide and conquer) and one is the actual operation of merging.

First use a while loop to check if the list has more than two linked list. If they have more than two linked
lists we simple pick the first two linked list and merge them together and add it back to the 'mergedList' 
ex:  [[1,2,3,4], [1,2,3,5], [2,3], [4,6,7], [3,4]] -> [[1,1,2,2,3,3,4,5],[2,3,4,6,7],[3,4]] -> and so on till
the list has been fully merged (log(k)) operation

Second write a function that merge the two linked list that has been passed in. O(N) operation.
Just make sure you realize you can apply divide and conquer to solve this problem
In total the time complexity would be O(N*log(k))
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        
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
                # condition for l2 to make sure that i + 1 will stay inbound
                # passing in None can still be linked by a linked list
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(mergeList(l1, l2))
            lists = mergedList
        return lists[0]
    