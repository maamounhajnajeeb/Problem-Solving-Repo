# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Example : input : letters = ["c","f","j"], target = "a"
#         : output: "c"
# Example : input : letters = ["c","f","j"], target = "c"
#         : output: "f"
# Example : letters = ["x","x","y","y"], target = "z"
#         : output: "x"
# Example : letters = ["c","f","j"], target = "d"
#         : output: "c"

class Solution:
    def result(self, letters:list[str], mid:int, target:str)->str:
        if letters[mid] > target:
            if mid-1 >= 0 and letters[mid-1] > target:
                return "left"
            return "found"
        elif letters[mid] < target or target == letters[mid]:
            return "right"

    def nextGreatestLetter(self, letters:list[str], target:str)->str:
        start, end = 0, len(letters)-1
        while start <= end:
            mid = (start+end)//2
            result = self.result(letters, mid, target)
            if result == "found":
                return letters[mid]
            elif result == "left":
                end = mid-1
            elif result == "right":
                start = mid+1
        return letters[0]
