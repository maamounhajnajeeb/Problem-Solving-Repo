# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# Example : input: words = ["abc","car","ada","racecar","cool"]
#         : Output: "ada"

# Example2: Input: words = ["def","ghi"]
#         : Output: ""

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        w: int = 0
        while w < len(words):
            word: str = words[w]
            i: int = 0
            j: int = len(word)-1
            k: str = ""
            while i <= j:
                if word[i] == word[j]:
                    k += word[i]
                    i += 1
                    j -= 1
                else:    
                    break
            if k == word[:i] and len(k) > (len(word) // 2) - 1:
                return word
            w += 1
        return ""
