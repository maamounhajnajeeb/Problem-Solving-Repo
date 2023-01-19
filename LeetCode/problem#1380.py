# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
  
# Example 2:
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

# The Solution #

from math import inf

class Solution:
    def findMin(self, row: list[int]) -> int:
        lower: int; c: int; i: int; length: int
        lower, c, i, length = inf, -1, 0, len(row)
        while i < length:
            number: int = row[i]
            if number < lower:
                lower, c = number, i
            i += 1
        return lower, c
    
    def isBiggest(self, matrix: list[list[int]], min: int, c: int):
        for i in range(len(matrix)):
            if matrix[i][c] > min:
                return False
        return True

    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        result: list[int]; i: int; c: int; length: int; minimum: int
        result, i, length = [], 0, len(matrix)
        while i < length:
            row: list[int] = matrix[i]
            minimum, c = self.findMin(row)
            isBiggest: int = self.isBiggest(matrix, minimum, c)
            if isBiggest:
                result.append(minimum)
            i += 1
        return result
