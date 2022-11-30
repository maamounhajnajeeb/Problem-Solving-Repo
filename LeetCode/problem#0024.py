# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#  Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

## The Recursive Solution ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre: Optional[ListNode]; curr: Optional[ListNode]; nextHead: Optional[ListNode]
        pre, curr, nextHead = None, head, head.next.next
        counter: int = 0
        while counter < 2 and curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr, counter = nxt, counter+1
        curr: Optional[Node] = pre
        while curr.next:
            curr = curr.next
        curr.next = self.swapPairs(nextHead)
        return pre
