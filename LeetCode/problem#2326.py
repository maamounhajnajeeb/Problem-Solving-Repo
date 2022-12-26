# You are given two integers m and n, which represent the dimensions of a matrix.

# You are also given the head of a linked list of integers.

# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix.
# If there are remaining empty spaces, fill them with -1.

# Return the generated matrix.

# Example 1:
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the matrix.
# Note that the remaining spaces in the matrix are filled with -1.

# Example 2:
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed from left to right in the matrix.
# The last space in the matrix is set to -1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        table: list[list[int]] = [[-1 for _ in range(n)] for _ in range(m)]
        T: int; L: int
        L, T = 0, 0
        while head:
            for j in range(L, n):
                if not head: 
                    return table
                table[T][j] = head.val
                head = head.next
            T += 1
            
            for j in range(T, m):
                if not head: 
                    return table
                table[j][n-1] = head.val
                head = head.next
            n -= 1
            
            for j in range(n-1, L-1, -1):
                if not head:
                    return table
                table[m-1][j] = head.val
                head = head.next
                
            m -= 1
            
            for j in range(m-1, T-1, -1):
                if not head: 
                    return table
                table[j][L] = head.val
                head = head.next
            L += 1
        return table
