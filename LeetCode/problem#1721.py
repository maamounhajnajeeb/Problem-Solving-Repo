# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Hint(1/2) : We can transform the linked list to an array this should ease things up
# Hint(2/2) : After transforming the linked list to an array it becomes as easy as swapping two integers in an array then rebuilding the linked list

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## The Solution ##

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1] Transorm to list
        curr: Optional[ListNode] = head
        Nodes: list[int] = []
        while curr:
            Nodes.append(curr.val)
            curr = curr.next
        
        # 2] find Index and find length
        length: int; lastIndex: int; firstIndex: int
        length = len(Nodes)
        firstIndex = k-1
        lastIndex = length-k
        
        # 3] swapping
        Nodes[firstIndex], Nodes[lastIndex] = Nodes[lastIndex], Nodes[firstIndex]
        
        # 4] Transform from Array Tot Linked-List
        curr: Optional[ListNode] = head
        counter: int = 0
        while curr:
            if counter == firstIndex:
                curr.val = Nodes[firstIndex]
            elif counter == lastIndex:
                curr.val = Nodes[lastIndex]
            counter += 1
            curr = curr.next
        
        return head
