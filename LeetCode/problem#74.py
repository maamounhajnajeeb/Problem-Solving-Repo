# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# * Integers in each row are sorted from left to right
# * The first integer of each row is greater than the last integer of the previous row.

# Example : Input : matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#         : Output: true

# Example : Input : matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#         : Output: false

class Solution:

    def BinarySearch(self, matrix:list[int], target:int)->bool:
        start, end = 0, len(matrix)-1
        while start <= end:
            mid = (start+end)//2
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                end = mid-1
            elif matrix[mid] < target:
                start = mid+1

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start, end = 0, len(matrix)-1
        while start <= end:
            mid = (start+end) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return self.BinarySearch(matrix[mid], target)
            elif mid > 0 and target < matrix[mid][0]:
                if self.BinarySearch(matrix[mid-1], target):
                    return True
                end = mid-1
            elif mid < len(matrix)-1 and target > matrix[mid][-1]:
                if self.BinarySearch(matrix[mid+1], target):
                    return True
                start = mid+1
            else:
                break

        return False
