# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# The Solution #

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        table = [[0 for _ in range(n)] for _ in range(n)]

        L: int; R: int; T: int; B: int
        L, R = 0, n
        T, B = 0, n
        counter: int = 1

        n = n**2
        while counter <= n:
            for j in range(L, R):
                table[T][j] = counter
                counter += 1
            T += 1
            for j in range(T, B):
                table[j][R-1] = counter
                counter += 1
            R -= 1
            for j in range(R-1, L-1, -1):
                table[B-1][j] = counter
                counter += 1
            B -= 1
            for j in range(B-1, T-1, -1):
                table[j][L] = counter
                counter += 1
            L += 1
        return table
