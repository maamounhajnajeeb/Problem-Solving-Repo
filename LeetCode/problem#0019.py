# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        curr: Optional[ListNode] = head
        counter: int = 0
        while curr:
            curr = curr.next
            counter += 1
        pre: Optional[ListNode]
        pre, curr = dummyNode, dummyNode.next
        newCounter: int = 1
        n = n-1
        while pre:
            if counter - newCounter == n:
                pre.next = curr.next
                return dummyNode.next
            else:
                pre, curr = curr, curr.next
                newCounter += 1
