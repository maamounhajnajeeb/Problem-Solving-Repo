# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet.
# return true if and only if the given words are sorted lexicographically in this alien language.

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match,
# and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅',
# where '∅' is defined as the blank character which is less than any other character (More info).

# First Solution #

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd: dict[str:int] = { c:i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            w1: str; w2:str
            w1, w2 = words[i], words[i+1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if orderInd[w1[j]] > orderInd[w2[j]]:
                        return False
                    break
        return True
      
# Second Solution #

class Solution:
    def filtering(self, fWord: str, sWord: str) -> tuple[str]:
        i: int; j: int; fLength: int; sLength: int
        i, j, fLength, sLength = 0, 0, len(fWord), len(sWord)
        while i < fLength and j < sLength and fWord[i] == sWord[j]:
            i, j = i+1, j+1
        return fWord[i:], sWord[j:]
    
    def studyCase(self, i:int, j:int, fLength: int, sLength: int, fWord:str, sWord:str) -> tuple[str]:
        if i == fLength:
            fLetter, sLetter = "@", sWord[j]
        elif j == sLength:
            sLetter, fLetter = "@", fWord[i]
        else:
            fLetter, sLetter = fWord[i], sWord[j]
        return fLetter, sLetter
    
    def comparison(self, fWord: str, sWord: str, hashTable: dict[str: int]) -> bool:
        fLength: int; sLength: int; i: int; j: int; fLetter: str; sLetter: str
        fLength, sLength, i, j = len(fWord), len(sWord), 0, 0
        while i < fLength or j < sLength:
            fLetter, sLetter = self.studyCase(i, j, fLength, sLength, fWord, sWord)
            if sLetter != fLetter:
                if hashTable[fLetter] > hashTable[sLetter]:
                    return False
                return True
            i, j = i+1, j+1
        return True if fLength == sLength else False
    
    def makingHashTable(self, order: str):
        hashTable: dict[str:int]; i: int; length: int; j: int
        hashTable, length, i, j = {}, len(order), 0, 1
        hashTable["@"] = 0
        while i < length:
            hashTable[order[i]] = j
            i, j = i+1, j+1
        return hashTable
    
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        length: int; i: int; hashTable: dict[str:int]; fWord: str; sWord:str
        length, i, hashTable = len(words), 0, self.makingHashTable(order)
        while i < length-1:
            fWord, sWord = self.filtering(words[i], words[i+1])
            if not self.comparison(fWord, sWord, hashTable):
                return False
            i += 1
        return True
