# Given two binary strings a and b, return their sum as a binary string.
# Example :
# input : a = "11", b = "1"
# output : "100"

class Solution:
    def counting(self, binary)->int:
        number, counter = 0, 0
        while counter < len(binary):
            if binary[counter] == "1":
                number = number + (2**(len(binary)-1-counter))
            counter += 1
        return number

    def addBinary(self, a: str, b: str) -> str:
        return bin(self.counting(a)+self.counting(b))[2:]
