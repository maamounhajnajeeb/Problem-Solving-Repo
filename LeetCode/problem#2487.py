# You are given the head of a linked list.
# Remove every node which has a node with a strictly greater value anywhere to the right side of it.
# Return the head of the modified linked list.

# Example 1:

# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:

# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.

# The O(n) Time Complexity Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        def reverse(head: Optional[ListNode]):
            curr: Optional[ListNode] = head
            pre: None = None
            while curr:
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            return pre

        head = reverse(head)
        maxSoFar = head.val
        
        dummy = ListNode()
        res = dummy
        
        while head:
            if maxSoFar <= head.val:
                maxSoFar = head.val
                res.next = ListNode(head.val)
                res = res.next
            head = head.next
        
        return reverse(dummy.next)
