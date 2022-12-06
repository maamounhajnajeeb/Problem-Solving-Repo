# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right,
# and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

# The Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        LPre, cur = dummyNode, head
        for i in range(left-1):
            LPre, cur = cur, cur.next
        
        pre: None =None
        for i in range(right-left+1):
            tmp : Optional[ListNode] = cur.next
            cur.next = pre
            pre, cur = cur, tmp

        LPre.next.next = cur
        LPre.next = pre

        return dummyNode.next
