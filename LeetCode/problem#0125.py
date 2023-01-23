# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    
    def twoPointers(self, text:str):
        i: int; j:int
        i, j = 0, len(text)-1
        while i < j:
            if text[i] != text[j]:
                return False
            i, j = i+1, j-1
        return True
    
    def valid(self, letters: dict[str:bool], letter: str) -> bool:
        try:
            letters[letter]
            return True
        except KeyError:
            return False

    def filteringText(self, text: str, letters: dict[str:bool]) -> str:
        i: int = 0
        while i < len(text) - 1:
            valid: bool = self.valid(letters, text[i])
            if not valid:
                text = text[:i]+text[i+1:]
            else:
                i += 1
        valid: bool = self.valid(letters, text[i])
        if not valid:
            text = text[:i]+text[i+1:]
        return text
    
    def isPalindrome(self, s: str) -> bool:
        allLetters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        letters: dict[str:bool] = {}
        for letter in allLetters:
            letters[letter] = True
        s = self.filteringText(s, letters)
        
        return self.twoPointers(s.lower())
