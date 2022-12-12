# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]

# The Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def __switching(self, curr: Optional[ListNode], dummy: Optional[ListNode]) -> tuple[Optional[ListNode]]:
        tmp: Optional[ListNode] = curr.next
        curr.next = None
        dummy.next = curr
        return dummy.next, tmp
    
    def __findUniqueNode(self, curr: Optional[ListNode], sec: Optional[ListNode]) -> Optional[ListNode]:
        while sec:
            if curr.val == sec.val:
                sec = sec.next
            else:
                return sec
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummyHead: Optional[ListNode] = ListNode()
        curr: Optional[ListNode]; dummyPointer: OptionalList[Node]
        curr, dummyPointer = head, dummyHead
        while curr:
            if curr.next:
                if curr.val == curr.next.val:
                    curr = self.__findUniqueNode(curr, curr.next)
                else:
                    dummyPointer, curr = self.__switching(curr, dummyPointer)
            else:
                dummyPointer, curr = self.__switching(curr, dummyPointer)
        return dummyHead.next
