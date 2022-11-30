# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

## The Solution ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1] slow, fast technique
        slow: Optional[ListNode]; fast: Optional[ListNode]
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        fast = None

        # 2] reveresing second half of the linked list
        second: Optional[ListNode] = slow.next
        slow.next = None
        reveresedSec = None
        while second:
            nxt = second.next
            second.next = reveresedSec
            reveresedSec = second
            second = nxt
        slow, second, nxt = None, None, None

        # 3] merging two halves
        sameFirst: Optional[ListNode] = head
        while sameFirst and reveresedSec:
            nxt = reveresedSec.next
            reveresedSec.next = sameFirst.next
            sameFirst.next = reveresedSec
            reveresedSec = nxt
            sameFirst = sameFirst.next.next
        reveresedSec, sameFirst = None, None

        # 4] return the reorder linked list
        return head
