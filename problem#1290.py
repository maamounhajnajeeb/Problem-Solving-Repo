# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

#  Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

## The Solution ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr: ListNode; i: int; binNum: int
        curr, i, binNum = head, 0, 0
        while curr.next:
            curr, i = curr.next, i+1
        while head:
            if head.val == 1:
                binNum += (2**i)
            i, head = i-1, head.next
        return binNum 
