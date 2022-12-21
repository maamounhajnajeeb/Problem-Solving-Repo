# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
  
# The Solution#

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res: list[int] = []
        L: int; R: int; T: int; B: int
        L, R = 0, len(matrix[0])
        T, B = 0, len(matrix)
        
        while L < R and T < B:
            
            for i in range(L, R):
                res.append(matrix[T][i])
            T += 1
            
            for i in range(T, B):
                res.append(matrix[i][R-1])
            R -= 1
            
            if not (L < R and T < B):
                return res
            
            for i in range(R-1, L-1, -1):
                res.append(matrix[B-1][i])
            B -= 1
            
            for i in range(B-1, T-1, -1):
                res.append(matrix[i][L])
            L += 1
        
        return res
