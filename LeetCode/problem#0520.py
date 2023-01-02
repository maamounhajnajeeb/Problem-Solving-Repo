# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Example 1:
# Input: word = "USA"
# Output: true

# Example 2:
# Input: word = "FlaG"
# Output: false

# The Solution #

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capsLetters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallLetters: str = "abcdefghijklmnopqrstuvwxyz"
        Letters: dict[str, str] = {}
        
        for i in range(len(capsLetters)):
            Letters[capsLetters[i]] = "Capital"
            Letters[smallLetters[i]] = "Small"
        
        if len(word) >= 2:
            if Letters[word[0]] == "Small" and Letters[word[1]] == "Capital":
                return False

        i: int = 0
        word = word[1:]
        while i < len(word)-1:
            first: str; second: str
            first, second = word[i], word[i+1]
            if Letters[first] != Letters[second]:
                return False
            i += 1
        return True
        
