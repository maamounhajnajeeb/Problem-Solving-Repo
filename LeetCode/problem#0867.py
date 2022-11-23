# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# Example 2:
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        firstRowLength: int = len(matrix[0])
        newMatrix: list[list[int]] = [[] for _ in range(firstRowLength)]
        x: int = 0
        while x < firstRowLength:
            y: int = 0
            rowNumber: int = len(matrix) 
            tempMatirx: list[int] = [[] for _ in range(rowNumber)]
            while y < rowNumber:
                tempMatirx[y] = matrix[y][x]
                y += 1
            newMatrix[x] = tempMatirx
            x += 1
        matrix = []
        return newMatrix
