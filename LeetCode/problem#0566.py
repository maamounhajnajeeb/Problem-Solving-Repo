# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
  
# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

# The Solution #

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        n: int; m: int; R: int; C: int; U: int
        n, m = len(mat[0]), len(mat)
        if (r*c) != (m*n): return mat
        table = [[0 for _ in range(c)] for _ in range(r)]
        R, C, U = 0, 0, 0
        while U < m:
            L: int = 0
            while L < n:
                table[R][C] = mat[U][L]
                C, L= C+1, L+1
                if C == c:
                    R, C = R+1, 0
            U += 1
        return table
