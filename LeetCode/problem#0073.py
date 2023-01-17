# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
  
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# The Solution #

class Solution:
    def editingWidth(self, length: int, width: list[int], matrix: list[list[int]]):
        x: int = 0
        while x < len(width):
            if width[x] == 0:
                for i in range(length):
                    matrix[i][x] = 0
            x += 1
        return matrix

    def editingHeight(self, secondaryLength: int, height: list[int], matrix: list[list[int]]):
        y: int = 0
        while y < len(height):
            if height[y] == 0:
                matrix[y] = [0 for _ in range(secondaryLength)]
            y += 1
        return matrix

    def setZeroes(self, matrix: list[list[int]]) -> None:
        length: int = len(matrix)
        secondaryLength: int = len(matrix[0])
        height: list[int] = [1 for _ in range(length)]
        width: list[int] = [1 for _ in range(secondaryLength)]
        i: int = 0
        while i < length:
            j: int = 0
            while j < secondaryLength:
                if matrix[i][j] == 0:
                    if height[i] != 0:
                        height[i] = 0
                    if width[j] != 0:
                        width[j] = 0
                j += 1
            i += 1
        matrix = self.editingWidth(length, width, matrix)
        matrix = self.editingHeight(secondaryLength, height, matrix)
