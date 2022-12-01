# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.
# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Example 1:
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.

# Example 2:
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]

# Example 3:
# Input: head = [1,2,3,-3,-2]
# Output: [1]

## The Solution ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashTable: dict[int:Optional[ListNode]] = {}
        dummyNode: Optional[ListNode] = ListNode()
        dummyNode.next = head
        curr = dummyNode
        sum: int = 0
        while curr:
            sum += curr.val
            if not sum in hashTable:
                hashTable[sum] = curr
            else:
                node: Optional[ListNode] = hashTable[sum]
                node.next = curr.next
                while sum != list(hashTable.keys())[-1]:
                    hashTable.popitem()
                hashTable[sum].next = curr.next
            curr = curr.next
        return dummyNode.next
