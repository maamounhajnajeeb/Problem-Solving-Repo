# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# Example : Input: n = 5
#           Output: 2

# Another example : Input: n = 8
#                   Output: 3

class Solution:
    def arrangeCoins(self, n : int):
        start, end = 0, n
        while start <= end:
            mid = (start+end)//2
            guess = mid*(mid+1)//2
            if guess > n:
                end = mid-1
            elif guess <= n:
                start = mid+1
                row = mid
        return row
