# Given a (m * n) matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example : Input : [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#         : Output: 8
# Another example : Input : [[3,2],[1,0]]
#                 : Output: 0


class Solution:
    
    def binary_search(self, row: list[int]) -> int:
        length = len(row)
        start, end = 0, length-1
        while start <= end:
            mid = (start+end) // 2
            if row[mid] < 0:
                if mid-1 >= 0 and row[mid-1] < 0:
                    end = mid-1
                else:
                    return length-mid
            else:
                start = mid+1
        return 0
    
    def countNegatives(self, matrix: list[list[int]]) -> int:
        count = 0
        for row in matrix:
            if row[-1] < 0:
                count += self.binary_search(row)
        return count

