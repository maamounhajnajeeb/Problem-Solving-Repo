# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummyNode: Optional[ListNode] = ListNode()
        dummyPointer: Optional[ListNode] = dummyNode
        while l1 and l2:
            if l1.val < l2.val:
                dummyPointer.next = l1
                l1 = l1.next
            else:
                dummyPointer.next = l2
                l2 = l2.next
            dummyPointer = dummyPointer.next
        if l1:
            dummyPointer.next = l1
        if l2:
            dummyPointer.next = l2
        return dummyNode.next

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists: list[Optional[ListNode]] = []
            for i in range(0, len(lists), 2):
                l1: Optional[ListNode] = lists[i]
                l2: Optional[ListNode] = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge2Lists(l1, l2))
            
            lists = mergedLists
        return lists[0]
