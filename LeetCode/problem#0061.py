# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

## First Solution ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __findLength(self, curr: Optional[ListNode]) -> int:
        length: int = 0
        while curr.next:
            length += 1
            curr = curr.next
        return length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr: Optional[ListNode] = head
        length: callable[[Optional[ListNode]], int] = self.__findLength(curr)
        
        if k == length+1 or k == 0: return head

        while k > length+1:
            k = k%(length+1)
        
        dummyNode: Optional[ListNode] = ListNode()

        pre: Optional[ListNode]
        pre, curr = head, head.next
        while length != k:
            pre, curr = curr, curr.next
            length -= 1
        dummyNode.next = curr
        pre.next = None
        pointer: Optional[ListNode] = dummyNode
        while pointer.next:
            pointer = pointer.next
        pointer.next = head
        return dummyNode.next

## Second Solution ##
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        length: int; tail: Optional[ListNode]
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        k = k%length
        if k == 0:
            return head
        
        curr: Optional[ListNode] = head
        for i in range(length-k-1):
            curr = curr.next
        newHead: Optional[ListNode] = curr.next
        curr.next = None
        tail.next = head
        return newHead
