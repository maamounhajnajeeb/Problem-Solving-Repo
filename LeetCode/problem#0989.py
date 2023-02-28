# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# Example 1:
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

# Example 2:

# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
  
# Example 3:
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021

class Solution:
    def extract_num(self, num: List[int]) -> int:
        a: int = 0
        for n in num:
            a = (a*10) + n
        return a

    def find_new_num(self, k: int):
        laLista: list[int] = []
        while k > 0:
            laLista.insert(0, k%10)
            k = k // 10
        return laLista

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k =  self.extract_num(num) + k
        num = self.find_new_num(k)
        return num
