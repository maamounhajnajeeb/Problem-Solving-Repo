# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

# Example1 : Input: num = 16
#            Output: true

# Example2 : Input: num = 14
#           Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # laLista = [i*i for i in range(1, num)]
        start, end = 0, num
        while start <= end:
            mid = (start+end) // 2
            if (mid*mid) == num:
                return True
            elif (mid*mid) > num:
                end = mid-1
            elif (mid*mid) < num:
                start = mid+1
        return False
