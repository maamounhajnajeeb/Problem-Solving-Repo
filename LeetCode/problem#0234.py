# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true

#Example 2:

# Input: head = [1,2]
# Output: false

# First Solution with O(N) Space Complexity #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        lista: list[int] = []
        while curr:
            lista.append(curr.val)
            curr = curr.next
        i: int; j: int
        i, j = 0, len(lista)-1
        while i < j:
            if lista[i] == lista[j]:
                i, j = i+1, j-1
            else:
                return False
        return True
        
# Second Solution with O(N) Space Complexity #
