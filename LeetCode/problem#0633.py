# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# Example: Input: c = 5
#          Output: true
#          Explanation: 1 * 1 + 2 * 2 = 5

# Example2: Input: c = 3
#           Output: false

from math import sqrt

class Solution:
    
    def leftBinSear(self, start: int, end: int, target: int):
        while start <= end:
            mid: int = (start+end) //2
            if (mid**2) > target: # maybe = also
                if mid-1 >= start and ((mid-1)**2) >= target: # maybe = also
                    end = mid-1
                else:
                    return mid
            elif (mid**2) < target:
                start = mid+1
            elif (mid**2) == target:
                return mid
        return start

    def rightBinSear(self, start: int, end: int, target: int): 
        while start <= end:
            mid: int = (start+end) //2
            if (mid**2) < target:
                if mid+1 <= end and ((mid+1)**2) <= target:
                    start = mid+1
                else:
                    return mid
            elif (mid**2) > target: # maybe = also
                end = mid-1
            elif (mid**2) == target:
                return mid
        return end

    def judgeSquareSum(self, c):
        rang: int = int(sqrt(c+1))
        i: int = 0
        j: int = rang
        while i <= j:
            condition: int = c-(j**2)
            if condition == (i**2):
                return i,j
            elif condition < (i**2):
                j = self.rightBinSear(i, j+1, c-(i**2))
            elif condition > (i**2):
                i = self.leftBinSear(i-1, j, condition)
        return False
