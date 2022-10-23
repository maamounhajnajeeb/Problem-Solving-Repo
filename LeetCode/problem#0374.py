# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Example : input : Input: n = 10, pick = 6
#         : outout : 6
#           input :  n = 1, pick = 1
#           output: 1

# The Solution # : 

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            mid = (start+end)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                end = mid-1
            elif result == 1:
                start = mid+1
