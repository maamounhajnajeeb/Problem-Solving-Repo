# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

## Two Solutions ##

# 1] Recursion Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyList = ListNode()
        curr = dummyList
        if list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                curr.next = self.mergeTwoLists(list1.next, list2)
            else:
                curr.next = list2
                curr = curr.next
                curr.next = self.mergeTwoLists(list1, list2.next)
        if not list1:
            curr.next = list2
        elif not list2:
            curr.next = list1
        return dummyList.next
      
# 2] Iteration Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyList = ListNode()
        curr = dummyList
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if not list1:
            curr.next = list2
        elif not list2:
            curr.next = list1
        return dummyList.next
