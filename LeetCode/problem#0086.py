# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# The Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # 1] verify if there is no nodes or there is only one
        if not head or not head.next: return head
        
        # 2] creating new linked lists
        dummyBig: Optional[ListNode] = ListNode()
        dummySmall: Optional[ListNode] = ListNode()
        
        # 3] assigning pointers
        bigPointer: Optional[ListNode]; smallPointer: Optional[ListNode]; curr: Optional[ListNode]
        bigPointer, smallPointer, curr = dummyBig, dummySmall, head
        
        # 4] looping through the head linked list and adding nodes to the new linked-list 
        while curr:
            tmp: Optional[ListNode] = curr.next
            curr.next = None
            if curr.val < x:
                smallPointer.next = curr
                smallPointer = smallPointer.next
            else:
                bigPointer.next = curr
                bigPointer = bigPointer.next
            curr = tmp
        
        # 5] take care of garbage data
        smallPointer.next = dummyBig.next
        head = dummySmall.next
        dummyBig, dummySmall = None, None
        
        # 6] returning the new head
        return head
