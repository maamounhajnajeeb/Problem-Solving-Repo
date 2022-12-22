# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# The Solution #

class Solution:
    def findTable(self, table: list[list[int]], n: int, R: int, L: int, T: int, B: int) -> list[list[int]]:
        while n > 0:
            for i in range(R-1, L-1, -1):
                table[T][i] = n
                n -= 1
            T += 1
            
            for i in range(T, B):
                table[i][L] = n
                n -= 1
            L += 1
            
            for i in range(L, R):
                table[B-1][i] = n
                n -= 1
            B -= 1
            
            for i in range(B-1, T-1, -1):
                table[i][R-1] = n
                n -= 1
            R -= 1

        return table
    
    def buildTable(self, n):
        table =[[0 for _ in range(n)] for _ in range(n)]
        L: int; R: int; T: int; B: int
        L, R = 0, n
        T, B = 0, n
        n = n**2
        return self.findTable(table, n, R, L, T, B)
    
    def spiralDiagonals(self, n: int) -> int:
        table = self.buildTable(n)
        
        sum : int = 0
        for i in range(n):
            sum += table[i][i]
            sum += table[i][-(i+1)]
        return sum-1
Sol = Solution()
print(Sol.spiralDiagonals(1001))
