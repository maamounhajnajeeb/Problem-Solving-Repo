# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
# Build the result list and return its head.

# Example 1:
# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

# Example 2:
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.

# The Solution #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __findB(self, aPointer: ListNode, limit: int):
        counter: int = 0
        while aPointer:
            if counter == limit:
                return aPointer
            aPointer = aPointer.next
            counter += 1

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pointer = list1
        counter: int = 0
        while pointer:
            if counter+1 == a:
                lastList2 = list2
                while lastList2.next:
                    lastList2 = lastList2.next
                lastList2.next = self.__findB(list1, b+1)
                pointer.next = list2
                return list1
            pointer = pointer.next
            counter += 1
