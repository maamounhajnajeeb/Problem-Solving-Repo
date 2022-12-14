# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
  
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def split(self, head: Optional[ListNode]) -> tuple[Optional[ListNode]]:
        slow: Optional[ListNode]; fast: Optional[ListNode]
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        tmp = slow.next
        slow.next = None
        slow = tmp
        return head, slow
        
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode: Optional[ListNode] = ListNode()
        dummyPointer = dummyNode
        while left and right:
            if left.val < right.val:
                dummyPointer.next = left
                left = left.next
            else:
                dummyPointer.next = right
                right = right.next
            dummyPointer = dummyPointer.next
        if left:
            dummyPointer.next = left
        elif right:
            dummyPointer.next = right
        return dummyNode.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        left: Optional[ListNode]; right: Optional[ListNode]
        left, right = self.split(head)
        
        left:callable[Optional[Node]: Optional[Node]] = self.sortList(left)
        right:callable[Optional[Node]: Optional[Node]] = self.sortList(right)
        
        return self.merge(left,right)
