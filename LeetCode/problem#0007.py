# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def inspectX(self, x: int) -> tuple[bool, int]:
        if x < 0:
            return True, -1*x 
        return False, x
        
    def swappingNum(self, x: int, status: bool) -> int:
        swappedNum: int; MAX: int
        swappedNum, MAX = 0, 2147483647
        while x > 0:
            reminder: int = x % 10
            x = x // 10
            if ((swappedNum > MAX // 10) or (swappedNum == MAX // 10 and reminder >= MAX % 10)):
                return 0
            swappedNum = (10*swappedNum) + reminder
        return swappedNum*-1 if status else swappedNum
    
    def reverse(self, x: int) -> int:
        inspect: tuple[bool, int] = self.inspectX(x)
        x = inspect[1]
        return self.swappingNum(x, inspect[0])
