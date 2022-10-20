# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Example : input:[1, 2, 3]
#           output:[1, 2, 4]
# Example : input:[9]
#           output:[1, 0]

class Solution:
    def plusOne(self, digits: list[int])-> list[int]:
        workingIndex = -1
        digits[workingIndex] += 1
        status = True
        while abs(workingIndex) <= len(digits) and status:
            status=False
            if digits[workingIndex] == 10:
                status=True
                digits[workingIndex] = 0
                try:
                    digits[workingIndex-1] += 1
                except IndexError:
                    return [1]+digits
            workingIndex -= 1
        return digits
