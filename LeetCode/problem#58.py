# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example:
# Input: s = "   fly me   to   the moon  "
# Output : 4

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, phraseCounter = len(s)-1, 0
        while i >= 0:
            if s[i] != " ":
                phraseCounter += 1
                if s[i-1] == " ":
                    break
            i -= 1
        return phraseCounter
