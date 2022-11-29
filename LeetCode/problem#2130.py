# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

## The Solution ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1] find length
        length: int = 0
        pointer:Optional[ListNode] = head
        while pointer.next:
            pointer, length = pointer.next, length+1
        
        # 2] find middle area
        counter: int = 0
        prePointer: Optional[ListNode]
        prePointer, pointer = None, head
        while counter <= (length//2):
            prePointer = pointer
            pointer, counter = pointer.next, counter+1
        
        # 3] reversing second half
        pre = None
        while pointer:
            nxt = pointer.next
            pointer.next = pre
            pre = pointer
            pointer = nxt
        
        # 4] merging two halves (first half and reveresed second half)
        prePointer.next = pre
        
        # 5] find max twin sum
            # 5.1] first of the reveresed second half
        prePointer = prePointer.next
            # 5.2] first of the not reveresed half is head
        sum: int = 0
        while prePointer:
            sum = max(sum, prePointer.val+head.val)
            head, prePointer = head.next, prePointer.next
        prePointer, head, pointer, pre, = None, None, None, None
        return sum
