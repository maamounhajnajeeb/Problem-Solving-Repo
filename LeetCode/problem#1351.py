# Given a (m * n) matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example : Input : [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#         : Output: 8
# Another example : Input : [[3,2],[1,0]]
#                 : Output: 0


class Solution:
    def binSearch(self, row):
        start, end = 0, len(row) - 1
        while start <= end:
            mid = (start + end) // 2
            if row[mid] < 0:
                if mid - 1 >= 0 and row[mid - 1] < 0:
                    end = mid - 1
                else:
                    return len(row) - mid
            elif row[mid] >= 0:
                start = mid + 1

    def countNegatives(self, grid: list[list[int]]) -> int:
        counter = 0
        for row in grid:
            if row[-1] < 0:
                counter += self.binSearch(row)
        return counter
