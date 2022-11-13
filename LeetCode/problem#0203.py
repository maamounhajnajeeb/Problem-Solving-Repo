# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:

# Input: head = [], val = 1
# Output: []

# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

## The Solution##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        if not current:
            return
        elif not current.next:
            if current.val == val: current = current.next
        prev = head
        current = head.next
        while current:
            if current.val == val:
                current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next
        if head:
            if head.val == val:
                head = head.next
        return head
