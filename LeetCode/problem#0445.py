# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
  
# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]

# Example 3:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def __helperLoop(self, head: Optional[ListNode], num: int) -> int:
        while head:
            num = num*10+head.val
            head = head.next
        return num

    def __buildLinkedList(self, sum: int) -> Optional[ListNode]:
        dummyNode: Optional[ListNode] = ListNode()
        dummyPointer = dummyNode
        if sum == 0:
            return dummyNode
        while sum > 0:
            dummyPointer.next = ListNode(sum%10)
            dummyPointer = dummyPointer.next
            sum //= 10
        return dummyNode.next
    
    def __reverseLList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre
    
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        num1: int; num2: int
        num1, num2 = 0, 0
        while l1 and l2:
            num1 = num1*10+l1.val
            num2 = num2*10+l2.val
            l1, l2 = l1.next, l2.next
        
        if not l1:
            num2 = self.__helperLoop(l2, num2)
        elif not l2:
            num1 = self.__helperLoop(l1, num1)
        
        sum: Optional[ListNode] = self.__buildLinkedList(num1+num2)
        
        return self.__reverseLList(sum)
